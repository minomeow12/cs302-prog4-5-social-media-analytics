"""
Evelyn Nguyen, CS302 Program 5, 12/05/25
This file implements the main application for the Social Media Analytics Tool.
"""

from __future__ import annotations
from typing import Optional
from social_media import  InsAcc, FbAcc, TiktokAcc
from data_structure import RBTree


class SocialMediaAnalytics: 

    """Constructor to initialize empty tree""" 
    def __init__(self):
        self._tree: RBTree = RBTree()

    """
        Main application to display menu 
    """ 
    def run(self) -> None:
        print("=" * 70)
        print(" " * 15 + "SOCIAL MEDIA ANALYTICS TOOL")
        print(" " * 10 + "Analyze Instagram, Facebook, and TikTok")
        print("=" * 70)
        
        while True:
            try:
                self._display_menu()
                choice = input("\nEnter your choice (1-9): ").strip()
                
                if choice == '1':
                    self._add_instagram_account()
                elif choice == '2':
                    self._add_facebook_account()
                elif choice == '3':
                    self._add_tiktok_account()
                elif choice == '4':
                    self._view_account()
                elif choice == '5':
                    self._view_all_accounts()
                elif choice == '6':
                    self._record_session()
                elif choice == '7':
                    self._update_follower_count()
                elif choice == '8':
                    self._display_statistics()
                elif choice == '9':
                    print("\n" + "=" * 70)
                    print("Thanks for using Social Media Analytics Tool!")
                    print("=" * 70)
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 8.")
                
                #pause for user to read output
                if choice in ['1', '2', '3', '4', '5', '6', '7','8']:
                    input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n" + "=" * 70)
                print("Application interrupted. Exiting...")
                print("=" * 70)
                break
            except EOFError:
                print("\n\nEnd of input detected. Exiting...")
                break
            except Exception as e:
                print(f"\nUnexpected error: {e}")
                print("Please try again")
    
    """Display the main menu options"""
    def _display_menu(self) -> None:
        print("\n" + "=" * 70)
        print(" " * 28 + "MAIN MENU")
        print("=" * 70)
        print("  1. Add Instagram Account")
        print("  2. Add Facebook Account")
        print("  3. Add TikTok Account")
        print("  4. View Specific Account")
        print("  5. View All Accounts (Sorted)")
        print("  6. Record Session Time")
        print("  7. Update Follower Count")
        print("  8. Display Analytics Statistics")
        print("  9. Exit")
        print("=" * 70)

    """
        Function to add a new Instagram account with posts and reels
    """   
    def _add_instagram_account(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 22 + "ADD INSTAGRAM ACCOUNT")
            print("=" * 70)
            
            username = self._get_non_empty_input("Enter username: ")
            followers = self._get_positive_int("Enter followers: ")
            minutes = self._get_positive_float("Enter avg daily minutes: ")
            
            account = InsAcc(username, followers, minutes)
            
            #Add posts
            print("\n--- Post Information ---")
            num_posts = self._get_positive_int("Enter number of posts to add: ", allow_zero=True)
            for i in range(num_posts):
                likes = self._get_positive_int(f"  Post {i+1} - Enter likes: ")
                account.add_post(likes)
            
            #Add reels
            print("\n--- Reel Information ---")
            num_reels = self._get_positive_int("Enter number of reels to add: ", allow_zero=True)
            for i in range(num_reels):
                views = self._get_positive_int(f"  Reel {i+1} - Enter views: ")
                account.add_reel(views)
            
            #use += operator overloading to add to tree
            self._tree += account
            
            print("\n" + "=" * 70)
            print(f"SUCCESS: Instagram account '{username}' added to the system!")
            print("=" * 70)
            
        except ValueError as e:
            print(f"\nVALUE ERROR: {e}")
            print("The account was not added. Please try again with valid values.")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
            print("The account was not added. Please check your input types.")
        except Exception as e:
            print(f"\nERROR: {e}")
            print("The account was not added.")

    """
        Function to add a new Facebook account with posts and groups
    """  
    def _add_facebook_account(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 22 + "ADD FACEBOOK ACCOUNT")
            print("=" * 70)
            
            username = self._get_non_empty_input("Enter username: ")
            followers = self._get_positive_int("Enter followers: ")
            minutes = self._get_positive_float("Enter avg daily minutes: ")
            
            account = FbAcc(username, followers, minutes)
            
            #Add posts
            print("\n--- Post Information ---")
            num_posts = self._get_positive_int("Enter number of posts to add: ", allow_zero=True)
            for i in range(num_posts):
                reactions = self._get_positive_int(f"  Post {i+1} - Enter reactions: ")
                account.add_post(reactions)
            
            #Join groups
            print("\n--- Group Information ---")
            num_groups = self._get_positive_int("Enter number of groups to join: ", allow_zero=True)
            for i in range(num_groups):
                group = self._get_non_empty_input(f"  Group {i+1} - Enter name: ")
                account.join_group(group)
            
            #Insert into tree
            self._tree.insert(account)
            
            print("\n" + "=" * 70)
            print(f"SUCCESS: Facebook account '{username}' added to the system!")
            print("=" * 70)
            
        except ValueError as e:
            print(f"\nVALUE ERROR: {e}")
            print("The account was not added. Please try again with valid values.")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
            print("The account was not added. Please check your input types.")
        except Exception as e:
            print(f"\nERROR: {e}")
            print("The account was not added.")

    """
        Function to a new TikTok account with videos and shares
    """ 
    def _add_tiktok_account(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 23 + "ADD TIKTOK ACCOUNT")
            print("=" * 70)
            
            username = self._get_non_empty_input("Enter username: ")
            followers = self._get_positive_int("Enter followers: ")
            minutes = self._get_positive_float("Enter avg daily minutes: ")
            
            account = TiktokAcc(username, followers, minutes)
            
            #Add videos
            print("\n--- Video Information ---")
            num_videos = self._get_positive_int("Enter number of videos to add: ", allow_zero=True)
            for i in range(num_videos):
                likes = self._get_positive_int(f"  Video {i+1} - Enter likes: ")
                account.add_video(likes)
                shares = self._get_positive_int(f"  Video {i+1} - Enter shares: ")
                account.add_share(shares)
            
            #Insert into tree
            self._tree.insert(account)
            
            print("\n" + "=" * 70)
            print(f"SUCCESS: TikTok account '{username}' added to the system!")
            print("=" * 70)
            
        except ValueError as e:
            print(f"\nVALUE ERROR: {e}")
            print("The account was not added. Please try again with valid values.")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
            print("The account was not added. Please check your input types.")
        except Exception as e:
            print(f"\nERROR: {e}")
            print("The account was not added.")

    """
        function to view details of a specific account by username
        Uses 'in' operator overloading for existence check
    """  
    def _view_account(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 25 + "VIEW ACCOUNT")
            print("=" * 70)
            
            username = self._get_non_empty_input("Enter username to view: ")
            
            # Use 'in' operator overloading
            if username in self._tree:
                account = self._tree.retrieve(username)
                if account:
                    print("\n" + "-" * 70)
                    print(account.display())
                    print(f"\nEngagement Rate: {account.engagement_rate():.4f} followers/minute")
                    print("-" * 70)
            else:
                print(f"\nWARNING: Account '{username}' not found in the system.")
                print("Please check the username and try again.")
                
        except ValueError as e:
            print(f"\nERROR: {e}")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
        except Exception as e:
            print(f"\nERROR: {e}")

    """
        Funcrtion to view all accounts in sorted order (by username)
        Uses len() operator overloading
    """ 
    def _view_all_accounts(self) -> None:
        try:
            # Use len() operator overloading
            if len(self._tree) == 0:
                print("\n" + "=" * 70)
                print("WARNING: No accounts in the system.")
                print("Please add accounts using options 1-3 from the main menu.")
                print("=" * 70)
                return
            
            print("\n" + "=" * 70)
            print(f" " * 20 + f"ALL ACCOUNTS (Total: {len(self._tree)})")
            print(" " * 22 + "(Sorted by Username)")
            print("=" * 70)
            
            displays = self._tree.display_all()
            for i, display in enumerate(displays, 1):
                print(f"\n[Account #{i}]")
                print(display)
                print("-" * 70)
                
        except Exception as e:
            print(f"\nERROR: {e}")

    """
    Function to record session time for an account
    Uses + operator overloading for adding minutes
    """  
    def _record_session(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 23 + "RECORD SESSION TIME")
            print("=" * 70)
            
            username = self._get_non_empty_input("Enter username: ")
            account = self._tree.retrieve(username)
            
            if account is None:
                print(f"\nWARNING: Account '{username}' not found in the system.")
                print("Please check the username and try again.")
                return
            
            minutes = self._get_positive_float("Enter session minutes to add: ")
            
            # Use + operator overloading
            account + minutes
            
            print("\n" + "=" * 70)
            print(f"SUCCESS: Added {minutes:.2f} minutes to '{username}'s session time.")
            print("=" * 70)
            
        except ValueError as e:
            print(f"\nVALUE ERROR: {e}")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
        except Exception as e:
            print(f"\nERROR: {e}")

    """
    function to update followe count
    """
    def _update_follower_count(self) -> None:
        try:
            print("\n" + "=" * 70)
            print(" " * 22 + "UPDATE FOLLOWER COUNT")
            print("=" * 70)
        
            username = self._get_non_empty_input("Enter username: ")
            account = self._tree.retrieve(username)
        
            if account is None:
                print(f"\nWARNING: Account '{username}' not found in the system.")
                print("Please check the username and try again.")
                return
        
            print(f"Current followers: {account.get_followers()}")
            new_followers = self._get_positive_int("Enter new follower count: ")
        
            account.update_followers(new_followers)
        
            print("\n" + "=" * 70)
            print(f"SUCCESS: Updated '{username}' to {new_followers} followers.")
            print("=" * 70)
        
        except ValueError as e:
            print(f"\nVALUE ERROR: {e}")
        except TypeError as e:
            print(f"\nTYPE ERROR: {e}")
        except Exception as e:
            print(f"\nERROR: {e}")

    """
        Function to display analyics statistics
        Uses recursive tree methods to gather data
    """   
    def _display_statistics(self) -> None:
        try:
            if len(self._tree) == 0:
                print("\n" + "=" * 70)
                print("WARNING: No accounts in the system.")
                print("Please add accounts to view statistics.")
                print("=" * 70)
                return
            
            print("\n" + "=" * 70)
            print(" " * 22 + "ANALYTICS STATISTICS")
            print("=" * 70)
            
            #get counts by type 
            instagram_count = self._tree.count_by_type("Instagram")
            facebook_count = self._tree.count_by_type("Facebook")
            tiktok_count = self._tree.count_by_type("TikTok")
            
            #get total followers 
            total_followers = self._tree.get_total_followers()
            
            print(f"\nTotal Accounts in System: {len(self._tree)}")
            print("-" * 70)
            print(f"  • Instagram Accounts: {instagram_count}")
            print(f"  • Facebook Accounts:  {facebook_count}")
            print(f"  • TikTok Accounts:    {tiktok_count}")
            print("-" * 70)
            print(f"\nTotal Followers Across All Platforms: {total_followers:,}")
            
            if len(self._tree) > 0:
                avg_followers = total_followers / len(self._tree)
                print(f"Average Followers per Account: {avg_followers:.2f}")
            
            print("=" * 70)
            
        except Exception as e:
            print(f"\nERROR: {e}")
    
    # -- INPUT VALIDATION HELPER METHODS --
    
    """
        Get non-empty string input with validation
        Args: prompt (str): The prompt to display
        Returns: str - validated non-empty string
        Raises: ValueError 
    """
    def _get_non_empty_input(self, prompt: str) -> str:
        while True:
            try:
                value = input(prompt).strip()
                if value == "":
                    print("Input cannot be empty. Please try again.")
                    continue
                return value
            except EOFError:
                raise ValueError("Input stream closed unexpectedly")
    
    """
        Get positive integer input with validation
        Args: 
            prompt (str): The prompt to display
            allow_zero (bool): Whether to allow 0 as valid input
        Returns: int 
        Raises: ValueError if input stream closed
    """
    def _get_positive_int(self, prompt: str, allow_zero: bool = False) -> int:
        while True:
            try:
                value = input(prompt).strip()
                if value == "":
                    print("Input cannot be empty. Please try again.")
                    continue
                
                num = int(value)
                
                if num < 0:
                    print("Value cannot be negative. Please try again.")
                    continue
                
                if not allow_zero and num == 0:
                    print("Value must be greater than 0. Please try again.")
                    continue
                
                return num      
            except ValueError:
                print("Invalid integer format. Please enter a whole number.")
            except EOFError:
                raise ValueError("Input stream closed unexpectedly")

    """
        Get positive float input with validation
        Args: prompt (str): The prompt to display
        Returns: float - validated non-negative float
        Raises: ValueError if input stream closed
    """  
    def _get_positive_float(self, prompt: str) -> float:
        while True:
            try:
                value = input(prompt).strip()
                if value == "":
                    print("Input cannot be empty. Please try again.")
                    continue
                
                num = float(value)
                
                if num < 0:
                    print("Value cannot be negative. Please try again.")
                    continue
                
                return num
                
            except ValueError:
                print("Invalid number format. Please enter a valid number.")
            except EOFError:
                raise ValueError("Input stream closed unexpectedly")


# MAIN FUNCTION 
def main():
    try:
        app = SocialMediaAnalytics()
        app.run()
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Application ztops unexpectedly.")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())