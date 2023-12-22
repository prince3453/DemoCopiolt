from flask import Flask, render_template
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Create a list to store the Fibonacci numbers
    fib = [0] * (n + 1)
    
    # Initialize the first two Fibonacci numbers
    fib[0] = 0
    fib[1] = 1
    
    # Compute the Fibonacci numbers using dynamic programming
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    # Return the nth Fibonacci number
    return fib[n]
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    if __name__ == '__main__':
        app.run()

# Test the function
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
