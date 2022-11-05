# Global variables in sdk_config

Global variables are almost never a good idea. In fact, I had to look up how to create them because it's never 
happened to me before. In this case, however, we gain a significant UX advantage by 
using global variables for our sdk configuration. It means the implementer of the sdk need not pass the sdk
object around. They can simply import resource classes directly after instantiating the sdk. 

This works here because no user needs to instantiate the sdk more than once. If the sdk were more abstract, requiring
multiple instantiations, this would not work.