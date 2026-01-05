"""
Evelyn Nguyen, CS302 Program 5, 12/05/25
This file implements a red-black tree data structure for managing social media accounts.
"""

from __future__ import annotations
from typing import Optional, List
from enum import Enum
from src.social_media import SocialMediaAccount

class Color(Enum):
    RED = 0
    BLACK = 1

class Node:
    """
        Constructor for Node
        Args: account (SocialMediaAccount): 
        Raises: TypeError if account is not a SocialMediaAccount
    """
    def __init__(self, account: SocialMediaAccount):
        if not isinstance(account, SocialMediaAccount):
            raise TypeError("account must be a SocialMediaAccount")
        self._account: SocialMediaAccount = account
        self._color: Color = Color.RED
        self._left: Optional[Node] = None
        self._right: Optional[Node] = None
        self._parent: Optional[Node] = None

    """
        Function to return the stored account
    """
    def get_account(self) -> SocialMediaAccount:
        return self._account
    
    """
        Function to return the node's color
    """
    def get_color(self) -> Color:
        return self._color
    
    """
        Function to set the node's color
        Args: color
        Raises: TypeError if color is not a Color enum
    """
    def set_color(self, color: Color) -> None:
        if not isinstance(color, Color):
            raise TypeError("Color must be a Color enum")
        self._color = color

    """
        Function to return the left child node
    """
    def get_left(self) -> Optional[Node]:
        return self._left
    
    """
        Function to sets the left child node
        Args: node
    """
    def set_left(self, node: Optional[Node]) -> None:
        self._left = node

    """
        Function to return the right child node
    """
    def get_right(self) -> Optional[Node]:
        return self._right
    
    """
        Function to sets the right child node
        Args: node
    """
    def set_right(self, node: Optional[Node]) -> None:
        self._right = node

    """
        Function to return the parent node
    """
    def get_parent(self) -> Optional[Node]:
        return self._parent
    
    """
        function to set the parent node
        arg: node
    """
    def set_parent(self, node: Optional[Node]) -> None:
        self._parent = node
    
class RBTree:
    """
        constructor to initialize empty tree
    """
    def __init__(self):
        self._root: Optional[Node] = None
        self._size: int = 0

    """
        Function to insert an account into the tree
        Args: SocialMediaAccount
        Raises:
            TypeError 
            ValueError if dup username found
    """
    def insert(self, account: SocialMediaAccount) -> None:
        if not isinstance(account, SocialMediaAccount):
            raise TypeError("Can only insert SocialMediaAccount obj")
        new_node = Node(account)
        self._root = self._insert_recursive(self._root, new_node, None)
        self._fix_insert(new_node)
        self._root.set_color(Color.BLACK)
        self._size += 1

    """
        Helper function to insert node into tree
        Arg:
            current: current node being examined
            new_node: node to insert
            parent: parent of the current node
        return: the node should be at this position
        raise ValueError if duplicate username found
    """
    def _insert_recursive(self, current: Optional[Node], new_node: Node, parent: Optional[Node]) -> Node:
        if current is None:
            new_node.set_parent(parent)
            return new_node
        if new_node.get_account() < current.get_account():
            current.set_left(self._insert_recursive(current.get_left(), new_node, current))
        elif new_node.get_account() == current.get_account():
            raise ValueError("Account already exist")
        else:
            current.set_right(self._insert_recursive(current.get_right(), new_node, current))
        return current
    
    """
        helper function to fix red-black tree properties after insertion
        arg: node - the newly inserted node
    """
    def _fix_insert(self, node: Node) -> None:
        while node != self._root and node.get_parent() and node.get_parent().get_color() == Color.RED:
            parent = node.get_parent()
            if parent:
                grandparent = parent.get_parent()
            else:
                grandparent = None
            if not grandparent:
                break
            if parent == grandparent.get_left():
                uncle = grandparent.get_right()
                if uncle and uncle.get_color() == Color.RED:
                    #case 1: uncle is red -> recolor
                    parent.set_color(Color.BLACK)
                    uncle.set_color(Color.BLACK)
                    grandparent.set_color(Color.RED)
                    node = grandparent
                else:
                    #case 2: uncle is black, node is right child
                    if node == parent.get_right():
                        node = parent
                        self._rotate_left(node)
                        parent = node.get_parent()
                        if parent:
                            grandparent = parent.get_parent() 
                        else:
                            grandparent = None
                    #case 3: Uncle is black, node is left child -> right rotate
                    if parent and grandparent:
                        parent.set_color(Color.BLACK)
                        grandparent.set_color(Color.RED)
                        self._rotate_right(grandparent)
            else:
                uncle = grandparent.get_left()
                if uncle and uncle.get_color() == Color.RED:
                    # Case 1: Uncle is red - recolor
                    parent.set_color(Color.BLACK)
                    uncle.set_color(Color.BLACK)
                    grandparent.set_color(Color.RED)
                    node = grandparent
                else:
                    # Case 2: Uncle is black, node is left child  -> right rotate
                    if node == parent.get_left():
                        node = parent
                        self._rotate_right(node)
                        parent = node.get_parent()
                        if parent:
                            grandparent = parent.get_parent() 
                        else:
                            grandparent = None
                    #case 3: Uncle is black, node is right child - left rotate
                    if parent and grandparent:
                        parent.set_color(Color.BLACK)
                        grandparent.set_color(Color.RED)
                        self._rotate_left(grandparent)
    
    """
        function to perform roate left around node
        arg: node to rotate around
    """
    def _rotate_left(self, node: Node) -> None:
        right_child = node.get_right()
        if not right_child:
            return
        
        node.set_right(right_child.get_left())
        if right_child.get_left():
            right_child.get_left().set_parent(node)
        
        right_child.set_parent(node.get_parent())
        
        if not node.get_parent():
            self._root = right_child
        elif node == node.get_parent().get_left():
            node.get_parent().set_left(right_child)
        else:
            node.get_parent().set_right(right_child)
        
        right_child.set_left(node)
        node.set_parent(right_child)

    """
        function to perform roate right around node
        arg: node to rotate around
    """
    def _rotate_right(self, node: Node) -> None:
        left_child = node.get_left()
        if not left_child:
            return
        
        node.set_left(left_child.get_right())
        if left_child.get_right():
            left_child.get_right().set_parent(node)
        
        left_child.set_parent(node.get_parent())
        
        if not node.get_parent():
            self._root = left_child
        elif node == node.get_parent().get_right():
            node.get_parent().set_right(left_child)
        else:
            node.get_parent().set_left(left_child)
        
        left_child.set_right(node)
        node.set_parent(left_child)

    """
        Function to retrieve an account by username 
        args: username (str)
        Returns: SocialMediaAccount if found, None otherwise
        Raises: 
            TypeError: if username is not a string
            ValueError: if username is empty
    """  
    def retrieve(self, username: str) -> Optional[SocialMediaAccount]:
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        if username.strip() == "":
            raise ValueError("username cannot be empty")     
        return self._retrieve_recursive(self._root, username.lower())

    """
        Helper function to perform recursive search for account by username
        Args:
            current: Current node being examined
            username: Username to find (lowercase)
        Returns: SocialMediaAccount if found, None otherwise
    """  
    def _retrieve_recursive(self, current: Optional[Node], username: str) -> Optional[SocialMediaAccount]:
        if current is None:
            return None
        
        current_username = current.get_account().get_username().lower()
        
        if username == current_username:
            return current.get_account()
        elif username < current_username:
            return self._retrieve_recursive(current.get_left(), username)
        else:
            return self._retrieve_recursive(current.get_right(), username)
        
    """
        Function to display all accounts in sorted order (in-order)
        Returns: list of formatted account strings
    """
    def display_all(self) -> List[str]:
        result = []
        self._display_recursive(self._root, result)
        return result
    
    """
        Helper function to traverse tree in-order and displays
        Args:
            current: Current node being examined
            result: list to  display strings
    """
    def _display_recursive(self, current: Optional[Node], result: List[str]) -> None:
        if current is None:
            return
        
        self._display_recursive(current.get_left(), result)
        result.append(current.get_account().display())
        self._display_recursive(current.get_right(), result)
    

    """
        Function to count accounts of a specific type 
        Args: account_type (str)
        Returns: int - the number of accounts of that type
    """
    def count_by_type(self, account_type: str) -> int:
        return self._count_by_type_recursive(self._root, account_type)
    
    """
        Helper function to count accounts of specific type
        Args:
            current: Current node
            account_type: Type to count
        Returns: Count of matching accounts
    """
    def _count_by_type_recursive(self, current: Optional[Node], account_type: str) -> int:
        if current is None:
            return 0
        
        count = 0
        display = current.get_account().display()
        
        if account_type in display:
            count = 1
        
        count += self._count_by_type_recursive(current.get_left(), account_type)
        count += self._count_by_type_recursive(current.get_right(), account_type)
        
        return count
    
    """
        Function to calculate total followers across all accounts (recursive)
        Returns: int - sum of all followers
    """
    def get_total_followers(self) -> int:
        return self._get_total_followers_recursive(self._root)

    """
        Helper function to sum all followers
        Args: current: Current node
        Returns: Sum of followers in this subtree
    """   
    def _get_total_followers_recursive(self, current: Optional[Node]) -> int:
        if current is None:
            return 0
        
        current_followers = current.get_account().get_followers()
        left_followers = self._get_total_followers_recursive(current.get_left())
        right_followers = self._get_total_followers_recursive(current.get_right())
        return current_followers + left_followers + right_followers

    """
        Function to return number of accounts in tree
        Returns: int, ythe number of accounts
    """ 
    def get_size(self) -> int:
        return self._size

    """
        Function to return root node (for testing purposes)
        Returns: Root node or None if tree is empty
    """  
    def get_root(self) -> Optional[Node]:
        return self._root
    
    # --- OPERATOR OVERLOADING ---
    """
        return size using len() operator
        Usage: len(tree)
    """  
    def __len__(self) -> int:
        return self._size
    
    """
        function to check if username exists using 'in' operator
        Usage: "username" in tree
        Args: username (str): 
        Returns: bool - True if found, False otherwise
    """ 
    def __contains__(self, username: str) -> bool:
        try:
            return self.retrieve(username) is not None
        except (TypeError, ValueError):
            return False
        
    """
        Add account using += operator
        Usage: tree += account
        Args: account (SocialMediaAccount): Account to add
        Returns: self (for chaining)
    """  
    def __iadd__(self, account: SocialMediaAccount) -> RBTree:
        self.insert(account)
        return self                




    
