# XDA Poster

I was always lazy to post a detail about my ROM updates on XDA forum.
Then I figured out a sweet solution to feed my laziness. The XDA API!!!

### What do you need to do to get it working?

* Export your XDA_KEY, and XDA_PASSWORD. It will be used to interacte with API Key.
* Install python3, pip, and firefox using your distro's package manager.
`pip install -U requirements.txt`

### Usage:
```python
from os import environ
XDA_KEY = environ['XDA_KEY']
xda = XDA(XDA_KEY)
thread_id = "3766138"
xda_post = "Hello World!"
xda.post(thread_id, xda_post)
# async can be used too
await post_async(thread_id, xda_post)
```
Your post must be posted on XDA if all things went right!


Thanks:

* [@yshalsager](https://github.com/yshalsager)
* [@shreejoy](https://github.com/shreejoy)

For pointing out this great API did exist! Google didn't show me anything about this API!
