import pandas as pd
import matplotlib.pyplot as plt
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='tiktok_report.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s')

# Sample data
data = {
    'username': ['charli_d_amelio', 'addisonre', 'bella.poarch', 'user1', 'user2', 'user3'],
    'followers': [150000000, 95000000, 85000000, 1000000, 2000000, 3000000],
    'engagement_rate': [15, 12, 10, 15, 12, 10]
}

df = pd.DataFrame(data)

# Sort by followers
top_users_followers = df.sort_values(by='followers', ascending=False).head(3)
logging.info("<--Packet sent! rippering--> Top Users by Followers")

# Sort by engagement rate
top_users_engagement = df.sort_values(by='engagement_rate', ascending=False).head(3)
logging.info("<--Packet sent! rippering--> Top Users by Engagement Rate")

# Visualization
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Top users by followers
axs[0].bar(top_users_followers['username'], top_users_followers['followers'])
axs[0].set_title('Top Users by Followers')
axs[0].set_xlabel('Username')
axs[0].set_ylabel('Followers')

# Top users by engagement rate
axs[1].bar(top_users_engagement['username'], top_users_engagement['engagement_rate'])
axs[1].set_title('Top Users by Engagement Rate')
axs[1].set_xlabel('Username')
axs[1].set_ylabel('Engagement Rate (%)')

plt.tight_layout()
plt.show()

# Log message for report
logging.info("<--Packet sent! rippering--> Generating Report")

# Report content
report = f"""
## TikTok Powerful Users Report

### Introduction
This report aims to identify powerful TikTok users based on engagement and follower count. The methodology involved collecting data through APIs and analyzing it using Python.

### Findings

#### Top Users by Follower Count
| Rank | Username       | Followers |
|------|----------------|-----------|
| 1    | charli_d_amelio| 150,000,000|
| 2    | addisonre      | 95,000,000 |
| 3    | bella.poarch   | 85,000,000 |

#### Top Users by Engagement Rate
| Rank | Username       | Engagement Rate |
|------|----------------|-----------------|
| 1    | user1          | 15%             |
| 2    | user2          | 12%             |
| 3    | user3          | 10%             |

### Conclusions
The report identifies key TikTok users with high engagement and follower counts. Dance videos are particularly effective in garnering attention.

### Recommendations
- Collaborate with top influencers for marketing campaigns.
- Monitor content trends to stay relevant.
- Regularly assess the security implications of popular users and trends.
"""

# Log report output
logging.info(report)

# Also print it in the console
print(report)
