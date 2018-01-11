### PythonExercise ###
echo "# PythonExercise" >> README.md\
git init\
git add README.md\
git commit -m "first commit"\
git remote add origin https://github.com/ooozbh/PythonExercise.git\
git push -u origin master\

## example ##


est Markdown document
=====================

Text
----

Here is a paragraph with bold text. **This is some bold text.** Here is a
paragraph with bold text. __This is also some bold text.__

Here is another one with italic text. *This is some italic text.* Here is
another one with italic text. _This is some italic text._

Here is another one with struckout text. ~~This is some struckout text.~~


Links
-----

Autolink: <http://example.com>

Link: [Example](http://example.com)

Reference style [link][1].

[1]: http://example.com  "Example"
[2]: sadfadf "sdf"


Images
------

Image: ![My image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

Headers
-------

# First level title
## Second level title
### Third level title
#### Fourth level title
##### Fifth level title
###### Sixth level title

### Title with [link](http://localhost)
### Title with ![image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

Code
----

```python
This
  is
    code
      fence
```

Inline `code span in a` paragraph.

This is a code block:

    /**
     * Sorts the specified array into ascending numerical order.
     *
     * <p>Implementation note: The sorting algorithm is a Dual-Pivot Quicksort
     * by Vladimir Yaroslavskiy, Jon Bentley, and Joshua Bloch. This algorithm
     * offers O(n log(n)) performance on many data sets that cause other
     * quicksorts to degrade to quadratic performance, and is typically
     * faster than traditional (one-pivot) Quicksort implementations.
     *
     * @param a the array to be sorted
     */
    public static void sort(byte[] a) {
        DualPivotQuicksort.sort(a);
    }

nothing  
    
Quotes
------

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

> A list within a blockquote:
>
> *	asterisk 1
> *	*asterisk 2*
> *	__asterisk 3__

> Formatting within a blockquote:
>
> ### header
> Link: [Example](http://example.com)



Html
-------

This is inline <span>html</html>.
And this is an html block.

<table>
  <tr>
    <th>Column 1</th>
    <th>Column 2</th>
  </tr>
  <tr>
    <td>Row 1 Cell 1</td>
    <td>Row 1 Cell 2</td>
  </tr>
  <tr>
    <td>Row 2 Cell 1</td>
    <td>Row 2 Cell 2</td>
  </tr>
</table>

Horizontal rules
----------------

---

___


***


Lists
-----

Unordered list:

*	asterisk 1
*	asterisk 2
*	asterisk 3


Ordered list:

1.	First
1.	Second
3.	Third


Mixed:

1. First
    *	asterisk 1
2. Second:
	* Fee
	* Fie
	* Foe
    *   jisdf
3. Third


Tables:

| asdfa     | asdfa     | sfdf      |
| ---       | ---       | ----      |
| safda     | asdfads   | safdadf   |
| adsf      | 111       | 123       |
