redlog
======

What you've read, everywhere


## Nick's speculative notes

[HTTP authentication, specifying user: npdoty]
	POST https://hostname/v1/read/
	{ user: 'npdoty',
	 read: [ 'guid-of-an-ATOM-feed-item-12345678',
	            'guid-of-an-ATOM-feed-item-78901234',
	            'http://example.org/story-I-read-without-RSS-just-in-browser',
	            'http://twitter.com/status/12345678992' ],
	 timestamp: 22233334444, //approximate time I read these items; we could do this per item, but whatevs
	 client-app: 'MyBrowser',
	 client-device: 'npdoty's MacBook Air'
	}

[HTTP authentication, specifying user: npdoty]
	GET https://hostname/v1/read/
	If-Modified-Since: Sat, 29 Oct 2012 19:43:31 GMT
	Accept: application/json

	HTTP 304 if no 'read' updates with timestamps since the If-Modified-Since date, otherwise:

	HTTP 200
	{ user: 'npdoty',
	 read: [ 'guid-of-an-ATOM-feed-item-12345678',
	            'guid-of-an-ATOM-feed-item-78901234',
	            'http://example.org/story-I-read-without-RSS',
	            'http://twitter.com/status/12345678' ]
	} 
	// that's all, the client doesn't care when you read an item, just that you read it at some point since they last asked.

Your clients (your local RSS client, your local Twitter client, your Web browser maybe, your phone's RSS client) all occasionally POST updates to hostname/v1/read/ when they have network access, to document when you read which things on the Web. Clients that want to avoid showing you things as unread will occasionally fetch (or often fetch with a conditional GET and get a quick 304 Unmodified response) to see which URLs and GUIDS you've already read. The server need not know anything about what subscriptions you have.

The server stores the data in a trivially-easy-to-index key-value store, with an index on timestamp descending.

This solves the read/unread problem on RSS feeds (as long as there's a common enough understanding of creating GUIDs in a consistent manner for each RSS item), but it also goes way farther. It solves Twitter read/unread status (no longer do I have to do that damn guessing scroll when I switch to a Twitter client on another device) and App.Net and any blogging/microblogging service that will come up in the future. And it even solves the problem (a problem we considered so fundamental that we've never even tried to solve it) of telling you when you've already read a link that you're about to follow on another browser or another device. What if someone posts the same item to Twitter and to their RSS feed and to their Facebook feed? If they could provide a consistent GUID to each one, your clients using this service would automatically know you'd already read it. And wouldn't you *love* to run the statistics on the list of read items and get an analysis of what you've been reading and when? Like a browsing history, but way more exhaustive. Finally, you could more conclusively answer the question: have I read this article before (instead of haphazardly searching your RSS readers and various devices' browsers' histories).
