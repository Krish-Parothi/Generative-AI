# This is Used for those document which don't have plain text (irrespective of any language).

# We have a Document which is not a plain text document, for e.g code file, markdown file, command line instructions..etc

# We use recursive Character Text Splitter 
# but with different type of keyword for these files.

# First, try to split along class definition
# "\nclass",
# "\ndef",
# "\n\tdef",

# Now Split by the normal type of lines
# "\n\n",
# "\n",
# " ",
# "",


from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return self.name"

    def is_passing(self):
        return self.grade >= 6.0


# Example usage
student1 = Student("Aarav", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
    print("The student is passing.")
else:
    print("The student is not passing.")

"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)
# Yaha Recursive Character Text Splitter ka Object Nahi Bana rhe , Yaha sirf from_language method ko call kr rhe hai.

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])