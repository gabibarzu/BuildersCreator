import csv
import sys


def toCamelCase(value):
    return value[0].lower() + value[1:]


def toPascalCase(value):
    return value[0].upper() + value[1:]


def generateClass(className):
    return f"""
public class {toPascalCase(className)}Builder
{{"""


def generateProperty(dataType, name):
    return f"""
    private {dataType} {toCamelCase(name)};"""


def generateMethod(className, dataType, name):
    return f"""
    public {toPascalCase(className)}Builder With{toPascalCase(name)}({dataType} value)
    {{
        this.{toCamelCase(name)} = value;
        return this;
    }}
"""


def generateBuildMethod(className, properties):
    return f"""
    public {toPascalCase(className)} Build() =>
        new {toPascalCase(className)}
        {{{generateBuildMethodBody(properties)}
        }};
}}"""


def generateBuildMethodBody(properties):
    body = ""
    for property in properties:
        name = property[1]
        body += generateAssertion(name)
    return body


def generateAssertion(name):
    return f"""
            {toPascalCase(name)} = this.{toCamelCase(name)},"""


def generateBuilders(className, file_name='input.csv', skip_header=True):
    try:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            with open(f'{className}Builder.cs', 'w') as f:
                f.write(generateClass(className))
                line_count = 0
                properties = []
                for row in csv_reader:
                    if line_count == 0 and skip_header:
                        line_count += 1
                        continue
                    properties.append(row)
                for property in properties:
                    dataType = property[0]
                    name = property[1]
                    f.write(generateProperty(dataType, name))
                f.write("\n")
                for property in properties:
                    dataType = property[0]
                    name = property[1]
                    f.write(generateMethod(className, dataType, name))
                f.write(generateBuildMethod(className, properties))
    except IOError:
        print("Please provide an existing input file.")


if (len(sys.argv) < 2):
    print("Please provide the area. The command should be *** python generator.py \"ClassName\" ***")
else:
    if (len(sys.argv) < 3):
        generateBuilders(sys.argv[1])
    else:
        skip_header = sys.argv[2].lower() == 'true'
        generateBuilders(sys.argv[1], sys.argv[2], skip_header)
