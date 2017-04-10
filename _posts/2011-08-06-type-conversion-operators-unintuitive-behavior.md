---
layout: post
status: publish
published: true
title: Type-Conversion Operators' Unintuitive Behavior
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 978
date: '2011-08-06 07:59:10 -0700'
date_gmt: '2011-08-06 14:59:10 -0700'
categories:
- computer science
tags:
- typedef
- type conversion
- operator
- compiler
- mangling
comments: []
---
A feature I only recently learned about are type-conversion operators. For any class, if you want to support type conversion to any type, you can do so by merely declaring (and of course defining) operators of the form _operator type()_:

```C++
class Widget {
  ...
  operator bool();
  operator thing();
  operator Foo();
  ...
}
```

While this is fine and dandy (and admittedly obviously attractive in ways), there is a big problem SEOmoz co-worker Brandon pointed out: __There's no way to determine which code path will be taken.__

For a little bit of context, I came across a set of type-conversion operators that seemed reasonable enough. They tried to cover the whole gamut of possible primitive types:

```C++
operator unsigned long long() const;

operator long long() const;

operator unsigned long() const { return operator unsigned long long(); }

operator long() const { return operator long long(); }

...
```

__The compiler has absolutely no problem with the above declaration.__ The class you put that in will happily compile, but the problem arises when you try to use it:

```C++
Widget w(...);

// Suddenly, the compiler complains, not knowing which operator to use
unsigned long int foo = w;
```

At this point, the compiler puts its foot down. What to me seems unintuitive is that even though there is an conversion operator to this exact type, the compiler won't use it. What's even more bizarre to me is that typedefs and in-header definitions can further muddle things up:

```C++
operator long long() const;

operator long() const;

operator int() const;

operator short() const;

// For whatever reason, let's say you do this:
operator int32_t() const {
    return operator long long();
}
```

__Even though int32_t will be the same as one of those other types, this will still compile.__ It makes a certain amount of sense when viewed in the context of the compiler because after all, it only does so much processing on headers because they're going to be directly included wherever you use them. __You actually don't get duplicate symbols in this case, and thus no "previously-defined" error.__ In reality, their function definitions are the same, and they actually get mangled to the same name (on my system the operators for int32_t and int both mangle to '_ZNK6WidgetcviEv'):

```bash
# See what mangled symbols actually appear
nm -j widget.o

# See what demangled symbols are actually there
nm -j widget.o | sed s/__/_/ | grep -v .eh | c++filt -n
```

The above (with in-header definitions) is exactly what we encountered in the code. We (well, a co-worker) suspected that the reason that the sort of multiple definition was allowed was that the names were getting mangled based on their typedef name string (mangled on int32_t instead of the actual type it maps to), but this is not the case. If you move the in-header definition for the int32_t operator into the .cpp file, the compiler will complain to you earlier.

My first inclination when dealing with the "conversion to type long long is ambiguous" error was to ask for an explicit conversion: static_cast<long long int>(myWidget). However, this doesn't work either. So even in this scenario, __you can't even ask for a specific type conversion operator.__ From what I can gather, type-conversion operators are a double-edged lightsaber: few things in C++ were added without a purpose, but it's extremely important to understand that exact purpose and its risks. To require that type conversions are __explicit__ you should generally use something like:

```C++
template <class T>

const T convert() const {
  ...
}

template <>
const bool convert<bool>() const {
  // Your conversion to bool
  ...
}
```
