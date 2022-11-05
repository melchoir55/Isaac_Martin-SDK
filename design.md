# Design Philosophy

Priority is always given to user experience. 

* We want intellij to be as effective as possible. 
* We want the user to only have to instantiate objects intuitively. That is, objects they are working with.
* We want the user to have to perform as little configuration and passing of objects as possible.

In order to accomplish these goals we often make design decisions which may be questionable in other systems. Some of these are discussed below.


# Possibly strange design decisions

## Global variables in sdk_config

Global variables are almost never a good idea. In fact, I had to look up how to create them because it's never 
happened to me before. In this case, however, we gain a significant UX advantage by 
using global variables for our sdk configuration. It means the implementer of the sdk need not pass the sdk
object around. They can simply import resource classes directly after instantiating the sdk. 

This works here because no user needs to instantiate the sdk more than once. If the sdk were more abstract, requiring
multiple instantiations, this would not work.

## Tests for ResourceBase are not comprehensive

Reflection is employed within some of these methods in order to minimize code for the resources
themselves. This means that the certain methods like `_process_response` cannot be tested in
isolation. You will find tests incorporating that method (and others) on the resources themselves.

## Some tests assume static criteria

Certain tests, such as the resource endpoints, test against specific kinds of data coming back
from the api. Since the state of these endpoints is static, this works just fine. Different
tests would be needed in an api whose data is dynamic.