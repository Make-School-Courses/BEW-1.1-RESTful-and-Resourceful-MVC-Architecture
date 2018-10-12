# Errors and Debugging

## Objectives

1. Read and interpret errors
1. Use Node's debugging tools
1. Google errors to understand them
1. Use errors to find out your next step

## Errors are Your Friends

Errors generally will tell you what is wrong with your code. Take the time to read them carefully and use them to solve your problems rapidly.

JavaScript errors you will see in two places. In your terminal (server errors) and in your console (client errors). In either case, errors have the same parts. An error type ("ReferenceError"), a specific error message ("num is not defined"), and then a **Stack Trace**.

![Error Example](assets/error-example.png)

The **Stack Trace** is the last commands the computer ran in reverse chronological error. Most of these commands happen on code you did not write and therefore cannot debug. However, usually the one line of code in the stack trace that you DID write is the one you need to fix.

When you want to Google an error, google the error type and the error message statement. e.g. `ReferenceError: num is not defined`.

### Types of JavaScript errors:

1. **RangeError** - A number "out of range" has occurred - 99% of the time you did math wrong.
1. **ReferenceError** - An illegal reference has occurred - 99% of the time you forgot to define a variable and then called something on it.
1. **SyntaxError** - A syntax error has occurred - 99% of the time you forgot a `,`, `}`, or a `)`.
1. **TypeError** - A type error has occurred - 99% of the time you called a function on the wrong type. e.g. `num.toUpperCase();` when `num` is an integer and `toUpperCase()` is a string function.
1. **URIError** - An error in encodeURI() has occurred - 99% of the time you screwed up the format of a URL or request.

## Resources

1. [Three Options to Debug Node](https://spin.atomicobject.com/2015/09/25/debug-node-js/)
1. [Node's Debugger](https://nodejs.org/api/debugger.html)
1. [node-inspector](https://github.com/node-inspector/node-inspector)
1. [Node Inspector (video)](https://www.youtube.com/watch?v=03qGA-GJXjI)
1. [Node.js's Errors](https://nodejs.org/api/errors.html#errors_class_referenceerror)

## Baseline Challenges

1. Use `console.log()` to debug the Giphy API tutorial's main route. Print out the `req` and Giphy API `response` objects.
  * Super long, too long to paste
1. Use Node's native debugger to do the same thing.
<<<<<<< HEAD
  * ''
1. Now use `node-inspector` to do the same thing.
  * Run node with argument 'inspect' with 'debugger' at breakpoint
=======
1. Now use `locus` to do the same thing.
>>>>>>> b4fe508d3ba1f57887737fb6d70e4749a647e200

1. Run these snippets of JS in your Node REPL (type `node` in your bash terminal) or in a repl.it console. Each will return an error. See what you would have to do to fix them so they did not throw an error.

	```js
	// 1
	var num = 2
	num.toPrecision(50)

	//2
	let x = 1;
	let y = 1;
	x = y + 1;

	//4
	var int = 1;
	int.toUpperCase();

	//3
	var horse = {
		height: 5
	};
	horse.height;

	//5
	let person = {
		eatsASandwhich : function() {
			return "yum"
		}
	};
	person.eatsASandwhich();

	// Run this lastt one in your browser's console
	//6
	eval("alert('Hello')");
	```

1. Read the following code snippet. What should it do? Can you run it in your console in your browser? What error do you get? Can you fix it?

	```js
	const peoplesNames = ["Dan", "Kathy", "Monika", "Carl"]

	let shortNames = [];
	let longNames = [];
	for (i = 0; i < peoplesNames.length; i++) {
	    if (peoplesNames[i].length < 4) {
		shortNames.push(peoplesNames[i])
		} else {
		longNames.push(peoplesNames[i])
	    }
	}
	console.log(shortNames);
	console.log(longNames);
	```
	  * The code snipped sorts short names(< 4 characters) and long names into respective arrays.  The error was an unexpected token, this was fixed by adding an opening bracket after the else statement.

![js-error-1](assets/js-error-1.png)
