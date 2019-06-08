# [Valid Number][title]

## Description

Validate if a given string can be interpreted as a decimal number.

Some examples:  
`"0"` => `true`  
`" 0.1 "` => `true`  
`"abc"` => `false`  
`"1 a"` => `false`  
`"2e10"` => `true`  
`" -90e3   "` => `true`  
`" 1e"` => `false`  
`"e3"` => `false`  
`" 6e-1"` => `true`  
`" 99e2.5 "` => `false`  
`"53.5e93"` => `true`  
`" --6 "` => `false`  
`"-+3"` => `false`  
`"95a54e53"` => `false`

**Note:** It is intended for the problem statement to be ambiguous. You should
gather all requirements up front before implementing one. However, here is a
list of characters that can be in a valid decimal number:

  * Numbers 0-9
  * Exponent - "e"
  * Positive/negative sign - "+"/"-"
  * Decimal point - "."

Of course, the context of these characters also matters in the input.

**Update (2015-02-10):**  
The signature of the `C++` function had been updated. If you still see your
function signature accepts a `const char *` argument, please click the reload
button to reset your code definition.


**Tags:** Math, String

**Difficulty:** Hard

## 思路

``` java
class Solution {
    public boolean isNumber(String s) {
        String strTrim = s.trim();
        int currentPos = 0;
        int sign = 1;
        if(strTrim.length() == 0){
            return false;
        }
        if(strTrim.charAt(0) == '+' || strTrim.charAt(0) == '-'){
            currentPos = 1;
            if(strTrim.charAt(0) == '-'){
                sign = -1;
            }
        }
        int eflag = 0;
        int dotflag = 0;
        for(int i=currentPos;i<strTrim.length();i++){
            if(Character.isLetter(strTrim.charAt(i))){
                if(strTrim.charAt(i) == 'e' && i!=currentPos && i!=strTrim.length()-1 && eflag!=1){
                    eflag = 1;
                    continue;
                } else{
                    return false;
                }
            }
            else if((strTrim.charAt(i) == '-' || strTrim.charAt(i) == '+') && i!=currentPos && i!=strTrim.length()-1){
                if(strTrim.charAt(i-1) == 'e'){
                    continue;
                } else{
                    return false;
                }
            }
            else if(strTrim.charAt(i) == '.' && i!=currentPos && i!=strTrim.length()-1  && dotflag!=1 && eflag!=1){
                 if(Character.isDigit(strTrim.charAt(i-1)) && (Character.isDigit(strTrim.charAt(i+1)) || strTrim.charAt(i+1) == 'e')){
                    dotflag = 1;
                    continue;
                } else{
                    return false;
                }
            } else if(strTrim.charAt(i) == '.' && i==currentPos && dotflag!=1 && eflag!=1){
                   if(i+1 < strTrim.length() && Character.isDigit(strTrim.charAt(i+1))){
                        dotflag = 1;
                        continue;
                    } else{
                        return false;
                    }
                }
            else if(strTrim.charAt(i) == '.' && i==strTrim.length()-1 && dotflag!=1 && eflag!=1){
                if(Character.isDigit(strTrim.charAt(i-1))){
                    dotflag = 1;
                    continue;
                } else{
                    return false;
                }
            }
            else if(Character.isDigit(strTrim.charAt(i))){
                continue;
            } else{
                return false;
            }
        }
        return true;
        
    }
}
```

[title]: https://leetcode.com/problems/valid-number
