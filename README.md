# BuildersCreator

This tool can be used to generate the C# class for the Design Pattern Builder class based on an input csv file.

## Execution

### Parameters
- `className` -> ClassName of the file
- `file_name` -> The input for the class properties that should be generated
- `skip_header` -> Flag that will skip the header for the csv input file

Using the python command `python generator.py "className"` and with an existing CSV file.

### Additional runnings example
- `python generator.py "className"`
- `python generator.py "className" "MyClass"`
- `python generator.py "className" "MyClass" True`

### File format
| DataType  | Name |
| ------------- | ------------- |
| string  | StringProperty  |
| int | IntProperty  |

The output will be placed in the file generated by the `className` and the `Builder.cs`.\
Example:`MyClassBuilder.cs` file.

## Build with

### Programming languages

- Python `3.5.x`

