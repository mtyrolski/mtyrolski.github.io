# Google Analytics Setup Guide

This repository comes with built-in support for Google Analytics. Follow this guide to set up Google Analytics tracking for your website.

## Overview

The site supports three different Google Analytics implementations:
- **Google Analytics 4 (GA4)** - Recommended for new websites
- **Universal Analytics** - Legacy version (sunset on July 1, 2023)
- **Classic Google Analytics** - Older legacy version

**We recommend using Google Analytics 4 (GA4)** as it's the current version supported by Google.

## Step 1: Create a Google Analytics Account

1. Go to [Google Analytics](https://analytics.google.com/)
2. Sign in with your Google account
3. Click **Start measuring** or **Admin** (gear icon)
4. Create an account:
   - Enter an **Account Name** (e.g., "Personal Website")
   - Configure account data sharing settings
   - Click **Next**

## Step 2: Set Up a Property

1. Enter a **Property Name** (e.g., "My GitHub Pages Site")
2. Select your **Reporting Time Zone**
3. Select your **Currency**
4. Click **Next**

## Step 3: Configure Property Details

1. Select your business category and size
2. Choose how you plan to use Google Analytics
3. Click **Create**
4. Accept the Terms of Service

## Step 4: Set Up Data Stream

1. Choose **Web** as your platform
2. Enter your website URL: `https://[your-github-username].github.io`
   - For example: `https://mtyrolski.github.io`
3. Enter a **Stream name** (e.g., "GitHub Pages Site")
4. Click **Create stream**

## Step 5: Get Your Measurement ID

After creating the data stream, you'll see your **Measurement ID** (also called Tracking ID). It looks like:
- **GA4 format**: `G-XXXXXXXXXX` (starts with "G-")
- **Universal Analytics format**: `UA-XXXXXXXXX-X` (starts with "UA-")

**Copy this ID** - you'll need it for the next step.

## Step 6: Configure Your Jekyll Site

1. Open the `_config.yml` file in your repository
2. Find the `analytics` section (around line 100-105):

```yaml
# Analytics
analytics:
  provider               : "false"
  google:
    tracking_id          : 
```

3. Update it with your Google Analytics settings:

**For Google Analytics 4 (Recommended):**
```yaml
# Analytics
analytics:
  provider               : "google-analytics-4"
  google:
    tracking_id          : "G-XXXXXXXXXX"
```

**For Universal Analytics (Legacy):**
```yaml
# Analytics
analytics:
  provider               : "google-universal"
  google:
    tracking_id          : "UA-XXXXXXXXX-X"
```

**For Classic Google Analytics (Legacy):**
```yaml
# Analytics
analytics:
  provider               : "google"
  google:
    tracking_id          : "UA-XXXXXXXXX-X"
```

4. Replace `G-XXXXXXXXXX` (or `UA-XXXXXXXXX-X`) with your actual Measurement ID
5. Save the file

## Step 7: Commit and Deploy

1. Commit your changes:
```bash
git add _config.yml
git commit -m "Add Google Analytics tracking"
git push
```

2. GitHub Pages will automatically rebuild your site (this may take a few minutes)

## Step 8: Verify Installation

1. Visit your website: `https://[your-github-username].github.io`
2. Open your browser's Developer Tools (F12)
3. Go to the **Network** tab
4. Refresh the page
5. Look for requests to:
   - `googletagmanager.com` (for GA4)
   - `google-analytics.com` (for Universal/Classic)

6. In Google Analytics:
   - Go to **Reports** → **Realtime**
   - You should see your visit appear within a few seconds

## Disabling Analytics on Specific Pages

If you want to disable analytics tracking on specific pages, add this to the page's front matter:

```yaml
---
title: "My Page"
analytics: false
---
```

## Troubleshooting

### Analytics not working?

1. **Check your tracking ID format**:
   - GA4 IDs start with `G-`
   - Universal Analytics IDs start with `UA-`
   - Make sure you're using the correct provider for your ID format

2. **Verify the configuration**:
   - Open `_config.yml` and ensure:
     - The provider is NOT set to `"false"`
     - The tracking_id is properly formatted with quotes
     - There are no extra spaces or typos

3. **Check if the site has rebuilt**:
   - Go to your repository on GitHub
   - Click on **Actions** tab
   - Check if the latest deployment succeeded (green checkmark)

4. **Verify the analytics code is included**:
   - View the page source of your website
   - Search for `gtag` (GA4) or `google-analytics.com` (Universal)
   - The tracking code should be present in the HTML

5. **Browser extensions**:
   - Ad blockers and privacy extensions may block Google Analytics
   - Try testing in an incognito/private window
   - Or temporarily disable extensions

6. **Clear your browser cache**:
   - Your browser might be showing a cached version of the site
   - Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)

### Data not showing in Google Analytics?

- It can take **24-48 hours** for data to appear in standard reports
- Check **Realtime** reports for immediate verification
- Make sure your site has actual visitors (visit it yourself!)

## Additional Features

### Event Tracking

Google Analytics 4 automatically tracks many events. To track custom events, you can use JavaScript in your pages:

```javascript
gtag('event', 'event_name', {
  'event_category': 'category',
  'event_label': 'label',
  'value': 1
});
```

### Enhanced Measurement

In your GA4 property settings, you can enable enhanced measurement for:
- Page views
- Scrolls
- Outbound clicks
- Site search
- Video engagement
- File downloads

To enable these:
1. Go to **Admin** → **Data Streams**
2. Click on your web stream
3. Toggle **Enhanced measurement** on
4. Click the gear icon to customize which events to track

## Privacy Considerations

When using Google Analytics, consider:

1. **Add a Privacy Policy**: Inform visitors about your use of analytics
2. **Cookie Consent**: Consider implementing a cookie consent banner for GDPR compliance
3. **IP Anonymization**: GA4 anonymizes IP addresses by default
4. **Data Retention**: Configure data retention settings in Google Analytics Admin

## Resources

- [Google Analytics 4 Documentation](https://support.google.com/analytics/answer/10089681)
- [GA4 Setup Guide](https://support.google.com/analytics/answer/9304153)
- [Migrating from Universal Analytics to GA4](https://support.google.com/analytics/answer/10759417)
- [Jekyll Analytics Documentation](https://jekyllrb.com/docs/)

## Support

If you encounter issues:
1. Check the [troubleshooting section](#troubleshooting) above
2. Review the [Google Analytics Help Center](https://support.google.com/analytics)
3. Open an issue in the repository with details about your problem
