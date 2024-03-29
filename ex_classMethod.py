class ExampleClass:
    class_variable = "I'm a class variable!"


    @classmethod
    def demo_class_method(cls):
        print(f"This is a class method. Accessing: {cls.class_variable}")



ExampleClass.demo_class_method()
