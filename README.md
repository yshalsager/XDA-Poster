# XDA Poster

I was always lazy to post a detail about my ROM updates on XDA forum.
Then I figured out a sweet solution to feed my laziness. The XDA API!!!

### What do you need to do to get it working?

* Export your XDA_USERNAME, and XDA_PASSWORD. It will be used to fetch the XDA API Key for further use.
* **YOUR PASSWORD IS NEVER STORED ANYWHERE, YOU CAN CHECK THE SOURCE, IF YOU DONT BELIEVE ME**
* Install python3, pip, and firefox using your distro's package manager.
`pip install -U requirements.txt`
* Get geckodriver from [here](https://github.com/mozilla/geckodriver/releases/latest) and extract to `/usr/local/bin/geckodriver`

### Usage:
```python
xda = XDA()
thread_id = "3766138"
xda_post_id = xda.get_post_id(thread_id)
xda_post = "Hello World!"
xda.post(xda_post_id, xda_post)
```
Your post must be posted on XDA if all things went right!


Thanks:

* [@yshalsager](https://github.com/yshalsager)
* [@shreejoy](https://github.com/shreejoy)

For pointing out this great API did exist! Google didn't show me anything about this API!
