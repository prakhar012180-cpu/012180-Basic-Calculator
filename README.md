<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Calculator in C - README</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --text-color: #c9d1d9;
            --border-color: #30363d;
            --code-bg: #161b22;
            --accent-color: #58a6ff;
            --header-border: #21262d;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            max-width: 880px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
        }

        h1 {
            font-size: 2rem;
            border-bottom: 1px solid var(--header-border);
            padding-bottom: 0.3em;
            color: #f0f6fc;
        }

        h2 {
            font-size: 1.5rem;
            border-bottom: 1px solid var(--header-border);
            padding-bottom: 0.3em;
            margin-top: 1.5rem;
            color: #f0f6fc;
        }

        h3 {
            font-size: 1.25rem;
            margin-top: 1rem;
        }

        p {
            margin-top: 0;
            margin-bottom: 16px;
        }

        ul, ol {
            padding-left: 2em;
            margin-bottom: 16px;
        }

        li {
            margin-bottom: 0.25em;
        }

        code {
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            background-color: rgba(110, 118, 129, 0.4);
            padding: 0.2em 0.4em;
            border-radius: 6px;
            font-size: 85%;
        }

        pre {
            background-color: var(--code-bg);
            border-radius: 6px;
            padding: 16px;
            overflow: auto;
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            font-size: 85%;
            line-height: 1.45;
            border: 1px solid var(--border-color);
        }

        pre code {
            background-color: transparent;
            padding: 0;
            border-radius: 0;
            font-size: 100%;
        }

        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: var(--border-color);
            border: 0;
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>Basic Calculator in C</h1>
    <p>A simple CLI-based calculator program written in C as part of the B.Tech programming laboratory course. It performs basic arithmetic operations based on user input.</p>

    <hr>

    <h2>Features</h2>
    <ul>
        <li><strong>Supported Operations:</strong> Addition (<code>+</code>), Subtraction (<code>-</code>), Multiplication (<code>*</code>), and Division (<code>/</code>).</li>
        <li><strong>Precision Output:</strong> Formats float results to 2 decimal places.</li>
        <li><strong>Error Handling:</strong>
            <ul>
                <li>Prevents division by zero with a clear warning message.</li>
                <li>Handles invalid operator inputs gracefully.</li>
            </ul>
        </li>
    </ul>

    <hr>

    <h2>How to Run</h2>

    <h3>Prerequisites</h3>
    <p>Make sure you have a C compiler (like <code>gcc</code>) installed on your system.</p>

    <h3>Steps</h3>
    <ol>
        <li>
            <strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/your-username/repository-name.git
cd repository-name</code></pre>
        </li>
        <li>
            <strong>Compile the code:</strong>
            <pre><code>gcc calculator.c -o calculator</code></pre>
        </li>
        <li>
            <strong>Run the program:</strong>
            <ul>
                <li>
                    On Linux/macOS:
                    <pre><code>./calculator</code></pre>
                </li>
                <li>
                    On Windows:
                    <pre><code>calculator.exe</code></pre>
                </li>
            </ul>
        </li>
    </ol>

    <hr>

    <h2>Sample Usage</h2>
    <pre><code>=========================================
        B.TECH LAB: BASIC CALCULATOR     
=========================================

Enter first number: 12.5
Enter an operator (+, -, *, /): *
Enter second number: 4

-----------------------------------------
Result: 12.50 * 4.00 = 50.00
-----------------------------------------</code></pre>

    <hr>

    <h2>Code Overview</h2>
    <ul>
        <li><code>scanf(" %c", &amp;op)</code>: Uses a leading space in the format string to bypass any leftover newline characters from prior input.</li>
        <li><code>switch(op)</code>: Handles operation selection efficiently.</li>
        <li><code>if (num2 != 0)</code>: Checks for zero division before attempting division operations.</li>
    </ul>

</body>
</html>
