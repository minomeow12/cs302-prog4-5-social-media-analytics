"""
1.Evelyn Nguyen, cs302 prog4, 11/26/25
2. This file is a python implementation of the social media core class hierarchy:
   Account (base), InsAcc, FbAcc, TiktokAcc (derived)
"""

from __future__ import annotations
from typing import List
import numpy as np
from abc import ABC, abstractmethod

# Base class for all social media accounts 
class SocialMediaAccount(ABC):
    """constructor"""
    def __init__(self, username: str, followers: int, avg_daily_minutes: float):
        # type check
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        if not isinstance(followers, int):
            raise TypeError("followers must be an int")
        if not isinstance(avg_daily_minutes, (int,float)):
            raise TypeError("avg_daily_minutes must be a number")

        # value check
        if username.strip() == "":
            raise ValueError("username cannot be empty")
        if followers < 0:
            raise ValueError("followers cannot be negative")
        if avg_daily_minutes < 0:
            raise ValueError("avg_daily_minutes cannot be negative")

        # protected instance variables
        self._username: str = username
        self._followers: int = followers
        self._avg_daily_minutes: float = float(avg_daily_minutes)

    # --- abstract methods ---
    """
    function to display summary of account info (abstract)
    arg: self, return string
    """
    @abstractmethod
    def display(self) -> str:
        raise NotImplementedError("Derived class must implement display()")
    
    """
    function to return a numpy array of three elemenst representing platform-specific metrics (abstract)
    returns: numpy array
    """
    @abstractmethod
    def get_engagement_stats(self) -> np.ndarray:
        raise NotImplementedError("Derived class must implement get_engagement_stats")
  
    # --- shared methods ---
    """
    function to add a session length to avg minutes and record it in numpy array
    arg: minutes(int | float) must be >= 0
    raise: TypeError and ValueError
    """
    def record_session(self, minutes: float) -> None:
        if not isinstance(minutes, (int, float)):
            raise TypeError("minutes must be a number")
        if minutes < 0:
            raise ValueError("minutes cannot be negative")
        self._avg_daily_minutes += float(minutes)

    """
    function to compute a simple engagement rate
    return: float: followers/avg_daily_minutes, 0 if avg_daily_minutes == 0
    """
    def engagement_rate(self) -> float:
        if self._avg_daily_minutes == 0:
            return 0.0
        return float (self._followers) / self._avg_daily_minutes

    """
    Function to update follower count
    Args: new_followers (int)
    Raises: TypeError, ValueError
    """ 
    def update_followers(self, new_followers: int) -> None:
        if not isinstance(new_followers, int):
            raise TypeError("new_followers must be an int")
        if new_followers < 0:
            raise ValueError("new_followers cannot be negative")
        self._followers = new_followers

    #--operator overloading--        
    """
    Less than comparison based on username (account1 < account2)
    """
    def __lt__(self, other: SocialMediaAccount) -> bool:

        if not isinstance(other, SocialMediaAccount):
            raise TypeError("Can only compare with SocialMediaAccount objects")
        return self._username.lower() < other._username.lower()

    """
    euqality comparison based on username
    usage: account1 == account2
    """
    def __eq__(self, other: object) -> bool:
       if not isinstance(other, SocialMediaAccount):
           return False
       return self._username.lower() == other._username.lower()

    """
        Add session minutes to account
        Usage: account + 15.5
    """
    def __add__(self, minutes: float) -> SocialMediaAccount:
        self.record_session(minutes)
        return self
    
    """getter functions"""
    def get_username(self) -> str:
        return self._username

    def get_followers(self) -> int:
        return self._followers

    def get_avg_daily_minutes(self) -> float:
        return self._avg_daily_minutes


# ---- derived class InsAcc ---
class InsAcc(SocialMediaAccount):
    """constructor"""
    def __init__(self, username: str, followers: int, avg_daily_minutes: float):
        super().__init__(username, followers, avg_daily_minutes)
        self._post_likes: List[int] = []
        self._reel_views: List[int] = []

    """
    function to record post's like count
    args: likes(int) non‑negative integer
    """
    def add_post(self, likes: int) -> None:
        if not isinstance(likes, int):
            raise TypeError("likes must be an int")
        if likes < 0:
            raise ValueError("likes cannot be negative")
        self._post_likes.append(likes)

    """
    function to record a reel's view count
    args: views(int) >= 0
    """
    def add_reel(self, views: int) -> None:
        if not isinstance(views, int):
            raise TypeError("views must be an int")
        if views < 0:
            raise ValueError("views cannot be negative")
        self._reel_views.append(views)

    
    """
    function to get_engagement_stats(self) -> np.ndarray:
    arg: self
    return np.array([total_posts, avg_post_likes, total_reel_views])
    """
    def get_engagement_stats(self) -> np.ndarray:
        total_posts = len(self._post_likes)
        if total_posts > 0:
            avg_post_likes = float(np.mean(self._post_likes)) 
        else:
            avg_post_likes = 0.0
        total_reel_views = int(sum(self._reel_views))
        return np.array([total_posts, avg_post_likes, total_reel_views], dtype=float)
    
    """
    function to return a formmatted summary for Ins Account
    return string
    """
    def display(self) -> str:
        stats = self.get_engagement_stats()
        return (
            f"Instagram Account: {self._username}\n"
            f"Followers: {self._followers}\n"
            f"Avg Daily Minutes: {self._avg_daily_minutes}\n"
            f"Total Posts: {int(stats[0])}, Avg Likes/Post: {stats[1]:.2f}, "
            f"Total Reel Views: {int(stats[2])}"
        )

# --- derived class FbAcc ---
class FbAcc(SocialMediaAccount):
    """constructor"""
    def __init__(self, username: str, followers: int, avg_daily_minutes: float):
        #invoke base
        super().__init__(username, followers, avg_daily_minutes)
        self._post_reactions: List[int] = []
        self._groups: List[str] = []
    
    
    """
    function to record reaction count for a FB post
    args: reactions(int) >=0
    raises: TypeError, ValueError
    """
    def add_post(self, reactions: int) -> None:
        if not isinstance(reactions, int):
            raise TypeError("reactions must be an int")
        if reactions < 0:
            raise ValueError("reactions cannot be negative")
        self._post_reactions.append(reactions)

    """
    function to join a FB group
    args: group(str): must be non-empty
    """
    def join_group(self, group_name: str) -> None:
        if not isinstance(group_name, str):
            raise TypeError("group must be a string")
        if group_name.strip() == "":
            raise ValueError("group cannot be empty")
        self._groups.append(group_name)

    """
    function to  Returns np.array([number_of_posts, average_reactions, number_of_groups])
    """
    def get_engagement_stats(self) -> np.ndarray:
        num_posts = len(self._post_reactions)
        if num_posts > 0:
            avg_reactions = float(np.mean(self._post_reactions))
        else:
            avg_reactions = 0.0
        num_groups = len(self._groups)
        return np.array([num_posts, avg_reactions, num_groups], dtype=float)

    """
    function to display summary for Facebook account
    """
    def display(self) -> str:
        stats = self.get_engagement_stats()
        return (
            f"Facebook Account: {self._username}\n"
            f"Followers: {self._followers}\n"
            f"Avg Daily Minutes: {self._avg_daily_minutes}\n"
            f"Total Posts: {int(stats[0])}, Avg Reactions/Post: {stats[1]:.2f}, "
            f"Groups: {int(stats[2])}"
        )
    
        


# --- derived class TiktokAcc ---
class TiktokAcc(SocialMediaAccount):
    """constructor"""
    def __init__(self, username: str, followers: int, avg_daily_minutes: float):
        super().__init__(username, followers, avg_daily_minutes)
        self._video_likes: List[int] = []
        self._shares: List[int] = []

    """
    function to add a video's like count
    args: likes(int) >= 0
    """
    def add_video(self, likes: int) -> None:
        if not isinstance(likes, int):
            raise TypeError("likes must be an int")
        if likes < 0:
            raise ValueError("likes cannot be negative")
        self._video_likes.append(likes)

    """
    function to record share count for a video
    args: shares(int) >= 0
    """
    def add_share(self, shares: int) -> None:
        if not isinstance(shares, int):
            raise TypeError("shares must be an int")
        if shares < 0:
            raise ValueError("shares cannot be negative")
        self._shares.append(shares)
    
    """
    fucntion to return np.array([total_videos, avg_likes, total_shares])
    """
    def get_engagement_stats(self) -> np.ndarray:
        total_videos = len(self._video_likes)
        if total_videos > 0:
            avg_likes = float(np.mean(self._video_likes))
        else:
            avg_likes = 0.0
        total_shares = int(sum(self._shares))
        return np.array([total_videos, avg_likes, total_shares], dtype=float)

    """
    function to return summary for TikTok account.
    """
    def display(self) -> str:
        stats = self.get_engagement_stats()
        return (
            f"TikTok Account: {self._username}\n"
            f"Followers: {self._followers}\n"
            f"Avg Daily Minutes: {self._avg_daily_minutes}\n"
            f"Total Videos: {int(stats[0])}, Avg Likes/Video: {stats[1]:.2f}, "
            f"Total Shares: {int(stats[2])}"
        )
