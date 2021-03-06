from ..utils import TranspileTestCase


class IfElifElseTests(TranspileTestCase):
    def test_if(self):
        # Matches if
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            """)

        # No match on if
        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Small x')
            """)

    def test_if_else(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            else:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Small x')
            else:
                print('Large x')
            """)

    def test_if_elif_else(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 100
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')
            """)

    def test_if_elif_elif_else(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            else:
                print('Huge x')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            else:
                print('Huge x')
            """)

        self.assertCodeExecution("""
            x = 100
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            else:
                print('Huge x')
            """)

        self.assertCodeExecution("""
            x = 1000
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            else:
                print('Huge x')
            """)

    def test_if_elif_elif(self):
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 10
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 100
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            """)

        self.assertCodeExecution("""
            x = 1000
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            elif x < 500:
                print('Large x')
            """)

    def test_multiple_if(self):
        # Make sure the most recent if block
        # is correctly identified.
        self.assertCodeExecution("""
            x = 1
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')
            print('Done 1.')

            x = 10
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')
            print('Done 2.')

            x = 100
            if x < 5:
                print('Small x')
            elif x < 50:
                print('Medium x')
            else:
                print('Large x')

            print('Done 3.')
            """)

    def test_multiple_if_is_comparison(self):
        # Make sure the most recent if block
        # is correctly identified.
        self.assertCodeExecution("""
            x = None
            if x is None:
                print('1: is none')
            else:
                print('1: is not none')
            print('Done 1.')

            if x is not None:
                print('2: is not none')
            else:
                print('2: is none')
            print('Done 2.')
            """)

    def test_end_of_block(self):
        # Ensure that the jump target at the end of a block
        # is correctly identified
        self.assertCodeExecution("""
            x = 100
            if x == 0:
                y = 42
            else:
                y = 37
            z = (x, y)
            print(z)
            print('Done')
            """)

    def test_simple_end_of_function_block_with_return(self):
        # Ensure that if the last instruction in an if block
        # is a return, a GOTO isn't added to the end of the block.
        self.assertCodeExecution("""
            def foo(x):
                print("Testing", x)
                if x == 0:
                    return 42
            y = foo(0)
            print("Result", y)
            y = foo(100)
            print("Result", y)
            print('Done')
            """)

    def test_end_of_function_block_with_return(self):
        # Ensure that if the last instruction in an if/else block
        # is a return, a GOTO isn't added to the end of the block.
        self.assertCodeExecution("""
            def foo(x):
                print("Testing", x)
                if x == 0:
                    return 42
            y = foo(0)
            print("Result", y)
            y = foo(100)
            print("Result", y)
            print('Done')
            """)

    def test_end_of_function_block_with_return_in_else(self):
        # Ensure that if the last instruction in an if/else block
        # is a return, a GOTO isn't added to the end of the block.
        self.assertCodeExecution("""
            def foo(x):
                print("Testing", x)
                if x == 0:
                    return 42
                else:
                    return 37
            y = foo(0)
            print("Result", y)
            y = foo(100)
            print("Result", y)
            y = foo(0)
            print("Result", y)
            print('Done')
            """)

    def test_end_of_block_in_main(self):
        # Ensure that the jump target at the end of a block
        # is correctly identified in a main loop
        self.assertCodeExecution("""
            print('Hello, World')
            if __name__ == '__main__':
                x = 100
                if x == 0:
                    y = 42
                else:
                    y = 37
            """, run_in_function=False)
