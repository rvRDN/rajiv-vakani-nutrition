# Retired public pages

These URLs belonged to the abandoned newsletter / supporters project. They are **not** part of the current public site. Old requests should return **HTTP 410 Gone** (see `_redirects`). They are not listed in `sitemap.xml`.

## Retired URLs

| Public URL | Former source (in Git) |
|---|---|
| `/table-talk.html` | `_archive/pages/table-talk.html` |
| `/table-talk` | same file (Pretty URL variant) |
| `/table-talk-archive.html` | `_archive/pages/table-talk-archive.html` |
| `/table-talk-archive` | same |
| `/no-onion-no-garlic.html` | `_archive/pages/no-onion-no-garlic.html` |
| `/no-onion-no-garlic` | same |
| `/no-onion-no-garlic-archive.html` | `_archive/pages/no-onion-no-garlic-archive.html` |
| `/no-onion-no-garlic-archive` | same |
| `/supporters.html` | `_archive/pages/supporters.html` |
| `/supporters` | same |
| `/members.html` | `_archive/pages/members.html` |
| `/members` | same |
| `/table-talk/support` | support path for Table Talk |
| `/no-onion-no-garlic/support` | support path for No Onion, No Garlic |

## Recover HTML from Git history

The HTML was removed from the working tree in commit `2a456e9` (“remove archived deploy files”). The last tree that still contained the pages is the parent:

```text
8e6cc348434451b7c3f967b10437c2a58d3a9639
```

Examples:

```bash
git show 8e6cc348434451b7c3f967b10437c2a58d3a9639:_archive/pages/table-talk.html
git show 8e6cc348434451b7c3f967b10437c2a58d3a9639:_archive/pages/no-onion-no-garlic.html
git show 8e6cc348434451b7c3f967b10437c2a58d3a9639:_archive/pages/supporters.html
```

To restore a copy locally for reading (do not put these back at the site root):

```bash
git show 8e6cc348434451b7c3f967b10437c2a58d3a9639:_archive/pages/table-talk.html > /tmp/table-talk.html
```

## Notes

- `/reference/*` still **301** redirects to `/therapy-profiles/:splat` (legitimate move, not retirement).
- Dead CSS class names (`.table-talk-card`, `.no-onion-no-garlic-card`) may remain in `rajiv-styles.css`; they do not create public URLs.
