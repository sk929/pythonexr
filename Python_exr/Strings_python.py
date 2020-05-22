Building strings with .format()
Python lets us concatenate strings with the + operator.

planet + ', we miss you.'
'Pluto, we miss you.'
If we want to throw in any non-string objects, we have to be careful to call str() on them first

position = 9
planet + ", you'll always be the " + position + "th planet to me."
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-23-73295f9638cc> in <module>
      1 position = 9
----> 2 planet + ", you'll always be the " + position + "th planet to me."

TypeError: must be str, not int
planet + ", you'll always be the " + str(position) + "th planet to me."
"Pluto, you'll always be the 9th planet to me."
This is getting hard to read and annoying to type. str.format() to the rescue.

"{}, you'll always be the {}th planet to me.".format(planet, position)
"Pluto, you'll always be the 9th planet to me."
So much cleaner! We call .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.

Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us.

If that was all that format() did, it would still be incredibly useful. But as it turns out, it can do a lot more. Here's just a taste:

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
"Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."


