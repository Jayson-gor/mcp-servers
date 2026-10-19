from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="YouTube Searcher")

FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"

@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 5):
    """Search recent freeCodeCamp YouTube videos by title and description.
    Every word in the query must appear in the title or description."""
    feed = feedparser.parse(FEED_URL)

    if not feed.entries:
        return [{"message": "Could not load the YouTube feed (no entries returned)."}]

    words = query.lower().split()
    results = []

    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("summary", "")

        haystack = f"{title} {description}".lower()

        if all(w in haystack for w in words):
            thumbs = entry.get("media_thumbnail", [])
            results.append({
                "title": title,
                "url": entry.get("link", ""),
                "published": entry.get("published", ""),
                "description": description,
                "thumbnail": thumbs[0].get("url", "") if thumbs else "",
            })
            if len(results) >= max_results:
                break

    return results or [{"message": f"No videos found among {len(feed.entries)} recent videos"}]

if __name__ == "__main__":
    mcp.run()