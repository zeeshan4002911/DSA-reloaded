From Java 11, we can run java single file using
java <FileName>.java

In many of the files the class name is not similar to FileName, because of this error will come on compilation on doing
javac <FileName>.java

For Java version < 11,
Make sure that file should have a public class with the same name as file name.

For Java version >= 11
We can directly run using java <FileName>.java
It will only look for main public method no matter class is Main or <FileName>
