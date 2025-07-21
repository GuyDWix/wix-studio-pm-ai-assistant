After investing the issue I have a couple of iinsights and ideas:

This issue is a combination of the following:
* the lightbox content container is set to pinned (position absolute) which causes it to be able to be bigger than it's wrapper parent (which is 100vh) without creating an inner scroll so the content cannot be revealed. 
* The website behind the lightbox modal's overlay is still scrollable although it is covered, which makes it look like it can be scrolled but it is not working. I do not understand how or why we don't block the scroll for the website while the lightbox is open
* We are missing the mentioned "full height" responsive package which can help with setting the lightbox to not hug an overly long content and show inner scroll inside itself
I think that the 1st and 2nd points should be investigated and see if there is a reason for why it is set the way it is today or not; for the product gap, this is good but is a secondary suggestion if we have the capacity for it
