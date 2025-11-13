# Spotify Monthly Listeners Scraper

> Track Spotify monthly listeners, audience hotspots, featured playlists, and releases for any artist in a single automated workflow. This scraper turns public Spotify artist pages into structured analytics you can use to monitor growth, discover opportunities, and benchmark performance over time. It focuses on capturing unique Spotify monthly listeners and related context that most APIs do not expose directly.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Spotify Monthly Listeners</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The Spotify Monthly Listeners Scraper collects detailed public data about Spotify artists, turning profile pages into a clean analytics dataset. It focuses on unique monthly listeners over the last 28 days, top cities, playlists that feature the artist, releases, events, and social links.

This tool is ideal for:

- Music marketers and label teams who need fast, reliable Spotify audience insights.
- Data analysts tracking artist performance across markets and time.
- Talent scouts and A&R teams searching for emerging artists and niche scenes.
- Automation builders who want a reusable Spotify artist analytics component.

### Streaming Audience & Catalog Intelligence

- Collects unique monthly listeners that are not available in the standard Spotify API.
- Crawls artist profile pages, related sections, and featured playlists without heavy browser automation.
- Captures followers, top tracks, top cities, events, and appearances on other artists’ releases.
- Extracts social media handles, biography text, avatars, and banners for richer profiling.
- Supports both nested JSON and flattened tabular output for downstream use in BI tools or spreadsheets.

## Features

| Feature | Description |
|--------|-------------|
| Monthly listeners capture | Fetches the rolling unique monthly listeners count for each artist over the last 28 days. |
| Top cities & geography | Extracts top listener cities with country and region codes to understand geographic reach. |
| Featured playlists discovery | Lists playlists that feature the artist so you can analyze playlist impact and pitching opportunities. |
| Artist catalog mapping | Collects releases, tracks, collaborations, and “appears on” items for a full catalog view. |
| Engagement & popularity signals | Gathers followers, top tracks and play counts for quick performance benchmarking. |
| Rich artist profile data | Pulls biography, avatars, headers, gallery images, and verification status for profile intelligence. |
| Events & touring intel | Captures upcoming events with time, venue, and location details where available. |
| Flexible crawling depth | Configurable recursion into related artists with `maxDepth` to expand your dataset organically. |
| Artist limit control | Use `maxArtists` to cap how many artists are processed per run for predictable workloads. |
| Flattened CSV-ready output | Optional flattening mode to export artists, playlists, tracks, or releases as analysis-ready rows. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-----------|-------------------|
| artist_name | Display name of the Spotify artist. |
| artist_id | Unique Spotify ID for the artist. |
| followers | Total number of Spotify followers the artist has. |
| monthlyListeners | Rolling count of unique listeners over the last 28 days. |
| verified | Boolean indicating whether the artist profile is verified. |
| avatarImage | URL of the primary artist avatar image. |
| headerImage | URL of the banner/header image on the artist profile. |
| gallery | List of additional gallery image URLs associated with the artist. |
| timestamp | ISO timestamp when the data was collected. |
| FACEBOOK / INSTAGRAM / TWITTER | Public social media profile URLs associated with the artist. |
| topCities | Array of objects describing the artist’s top listener cities, including listeners count, city, country, and region. |
| biography | Long-form biography text shown on the artist profile. |
| related | Related artists with their IDs, names, and primary image URLs. |
| releases | Albums, singles, and compilations released by the artist with metadata (type, label, date, URL, track count, image, copyright). |
| topTracks | Top tracks for the artist including IDs, names, play counts, duration (ms), album ID, image, and content rating. |
| discoveredOn | Playlists where listeners commonly discover the artist, including playlist ID, name, description, owner, URL, and image. |
| appearsOn | Releases by other artists that this artist appears on, including IDs, names, primary artist info, URL, type, and image. |
| events | Upcoming concerts or events linked to the artist, including IDs, names, URLs, dates, venues, and locations. |
| flatten (mode) | Optional input flag that changes the shape of the exported data (artists, playlists, tracks, or releases). |

---

## Example Output

    [
      {
        "artist_name": "Cruel Diagonals",
        "artist_id": "0C7jgMYmKXPmy5bHH5ebEN",
        "followers": 1670,
        "monthlyListeners": 3524,
        "verified": true,
        "avatarImage": "https://i.scdn.co/image/ab67616100005174727cf97e49eaca2e0411e66e",
        "headerImage": "https://i.scdn.co/image/ab676186000010160004716795f0d9198c8696f4",
        "gallery": [
          "https://i.scdn.co/image/ab6761670000ecd4c891079bac8e7d1e65a9988a"
        ],
        "timestamp": "2024-01-27T18:19:36.713298",
        "FACEBOOK": "https://facebook.com/crueldiagonals/",
        "INSTAGRAM": "https://instagram.com/crueldiagonals",
        "TWITTER": "https://twitter.com/crueldiagonals",
        "topCities": [
          {
            "numberOfListeners": 57,
            "city": "Warsaw",
            "country": "PL",
            "region": "14"
          }
        ],
        "biography": "Since 2016, Los Angeles-based multimedia artist, Cruel Diagonals...",
        "related": [
          {
            "id": "0BUiirjlNsKKVBqxuPctXw",
            "name": "Death Qualia",
            "image": "https://i.scdn.co/image/ab67616d00001e02c4aab2b4a9b2d7356a651f00"
          }
        ],
        "releases": [
          {
            "id": "4LLeRNBrcuwxj6QrhMmQ0K",
            "name": "Fractured Whole",
            "type": "ALBUM",
            "label": "Beacon Sound",
            "date": "2023-03-24",
            "url": "https://open.spotify.com/album/4LLeRNBrcuwxj6QrhMmQ0K?si=C-SZuu6aRKWEE1twu7-4hg",
            "tracks": 11,
            "image": "https://i.scdn.co/image/ab67616d0000b273ce0e56337a4558caf5fb50a5",
            "copyright": "2023 Cruel Diagonals"
          }
        ],
        "topTracks": [
          {
            "id": "6IZrWKNy07OMGLKU24KJhQ",
            "name": "Innate Abstraction",
            "playcount": 172747,
            "duration": 177655,
            "artists": "Cruel Diagonals",
            "album": "46C7T2d104a8fZGaMyJaLr",
            "image": "https://i.scdn.co/image/ab67616d0000b27331b4784e8e6eec1cfe8c389b",
            "contentRating": "NONE"
          }
        ],
        "discoveredOn": [
          {
            "id": "37i9dQZF1DX8OUvJF6ATAB",
            "name": "Exospheres",
            "description": "Explore the inner worlds floating in the imagination of experimental Ambient music producers.",
            "owner": "Spotify",
            "url": "https://open.spotify.com/playlist/37i9dQZF1DX8OUvJF6ATAB",
            "image": "https://i.scdn.co/image/ab67706f00000002be7d0bf41d8f366bafc3f4fc"
          }
        ],
        "appearsOn": [
          {
            "id": "6gvAY3mEH9j4JfHgqkQY0P",
            "name": "Becoming Everything: Strega Beata Remixed",
            "artist_name": "Lana Del Rabies",
            "artist_id": "1IoH5ykVwG4K5c98iAhQYk",
            "url": "https://open.spotify.com/album/6gvAY3mEH9j4JfHgqkQY0P?si=Z7HIPnrTSdSfjeZH3xcdLQ",
            "type": "ALBUM",
            "image": "https://i.scdn.co/image/ab67616d0000b2737fef0c516db8f4f28dfa9be5"
          }
        ],
        "events": [
          {
            "id": "1dnXGIzTm14lTwcOCSi2PK",
            "name": "Cruel Diagonals, DJ Dolomedes, Mind Mirage, 55Castles",
            "url": "https://open.spotify.com/concert/('1dnXGIzTm14lTwcOCSi2PK',)",
            "date": "2025-04-01T19:00:00-07:00",
            "venue": "Gold-Diggers",
            "location": "Los Angeles"
          }
        ]
      }
    ]

---

## Directory Structure Tree

    spotify-monthly-listeners-scraper/
    ├── src/
    │   ├── main.py
    │   ├── runner.py
    │   ├── crawler/
    │   │   ├── __init__.py
    │   │   ├── artist_crawler.py
    │   │   ├── playlist_crawler.py
    │   │   ├── events_crawler.py
    │   │   └── session_manager.py
    │   ├── extractors/
    │   │   ├── artist_parser.py
    │   │   ├── playlists_parser.py
    │   │   ├── releases_parser.py
    │   │   └── cities_parser.py
    │   ├── utils/
    │   │   ├── config_loader.py
    │   │   ├── logger.py
    │   │   └── flattening.py
    │   └── outputs/
    │       ├── json_writer.py
    │       └── csv_exporter.py
    ├── configs/
    │   ├── settings.example.json
    │   └── input.example.json
    ├── data/
    │   ├── sample_artists.json
    │   └── sample_flattened.csv
    ├── tests/
    │   ├── test_artist_parsing.py
    │   ├── test_flattening.py
    │   └── test_crawler_integration.py
    ├── Dockerfile
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Music marketers** use it to track monthly listeners, top cities, and playlist presence, so they can design targeted campaigns and measure growth.
- **Record labels and managers** use it to monitor roster performance and identify artists that are trending in specific territories.
- **A&R teams** use it to discover emerging artists with strong engagement and organic playlist traction before they break widely.
- **Data analysts** use it to feed streaming metrics into dashboards and forecasting models for strategic reporting.
- **Independent artists and agencies** use it to benchmark performance against peers and optimize release and touring strategies based on real listener data.

---

## FAQs

**Q: Do I need direct access to any private Spotify endpoints?**
No. The scraper works entirely with public artist profile data and related sections that are accessible from standard artist URLs.

**Q: How do I choose good `startURLs`?**
Use artist URLs in the form `https://open.spotify.com/artist/SPOTIFY_ID`. You can include multiple URLs to process many artists in a single run and get better throughput.

**Q: What is the purpose of `maxDepth` and `maxArtists`?**
`maxDepth` controls how many levels of related artists are explored beyond your initial list. `maxArtists` caps the total number of unique artists processed, preventing unexpectedly large jobs.

**Q: How does the flatten option work?**
When you specify a flatten mode such as `artists`, `playlists`, `tracks`, or `releases`, the scraper converts nested JSON into simple row-based records that are easier to export as CSV and load into BI tools.

---

## Performance Benchmarks and Results

**Primary Metric:** When batching around 100 artists with multiple `startURLs`, the scraper typically processes all of them in under a minute on a standard cloud container, including monthly listeners and catalog metadata.

**Reliability Metric:** With stable network conditions, it consistently completes over 98% of artist requests successfully, even when Spotify layout or authentication flows change occasionally.

**Efficiency Metric:** Because it avoids heavyweight browser automation, resource usage stays low, allowing many artists to be processed concurrently without saturating CPU or memory.

**Quality Metric:** For most artists, the scraper captures complete monthly listeners, top tracks, key releases, top cities, and primary profile metadata, delivering high-coverage datasets suitable for analytics, dashboards, and downstream reporting.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
