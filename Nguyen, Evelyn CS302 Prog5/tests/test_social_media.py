"""
1.Evelyn Nguyen, cs302 prog5, 11/30/25
2. This file is a python implementation of the social media testing file
   Including tests for social_media.py and data_structure.py
"""

import pytest
import numpy as np
from src.social_media import SocialMediaAccount, InsAcc, FbAcc, TiktokAcc
from src.data_structure import RBTree, Node, Color

#---Base class test---
"""constructor test """
def test_account_constructor_valid():
    acc = InsAcc("testuser", 100, 30.0)
    assert acc._username =="testuser"
    assert acc._followers == 100
    assert acc._avg_daily_minutes == 30.0

def test_account_constructor_empty_username():
    with pytest.raises(ValueError):
        InsAcc("", 100, 30)

def test_account_constructor_negative_followers():
    with pytest.raises(ValueError):
        InsAcc("abc", -10, 20)

def test_account_constructor_negative_minutes():
    with pytest.raises(ValueError):
        InsAcc("abc", 10, -20)

def test_base_constructor_wrong_types():
    with pytest.raises(TypeError):
        InsAcc(123, 10, 20)
    with pytest.raises(TypeError):
        InsAcc("abc", 1.5, 20)
    with pytest.raises(TypeError):
        InsAcc("abc", 10, "twenty")

def test_account_constructor_whitespace_username():
    with pytest.raises(ValueError):
        InsAcc("   ", 100, 30)

def test_account_constructor_int_minutes():
    acc = InsAcc("user", 100, 10)
    assert isinstance(acc._avg_daily_minutes, float)
    assert acc._avg_daily_minutes == 10.0

"""record_session() test """
def test_record_session_valid():
    acc = InsAcc("evelyn", 100, 30)
    acc.record_session(10)
    assert acc._avg_daily_minutes == 40

def test_record_session_negative():
    acc = InsAcc("eva", 100, 30)
    with pytest.raises(ValueError):
        acc.record_session(-5)

def test_record_session_invalid_type():
    acc = InsAcc("eva", 40, 10)
    with pytest.raises(TypeError):
        acc.record_session("abc")

def test_record_session_with_int():
    acc = InsAcc("user", 100, 10.0)
    acc.record_session(5)
    assert acc._avg_daily_minutes == 15.0

"""enagagement_rate() test """
def test_engagement_rate_zero_minutes():
    acc = InsAcc("eva", 100, 0)
    assert acc.engagement_rate() == 0

def test_engagement_rate_normal():
    acc = InsAcc("eva", 100, 20)
    assert acc.engagement_rate() == 100 / 20

"""update_followers() test"""
def test_update_followers_valid():
    acc = InsAcc("user", 100, 10.0)
    acc.update_followers(200)
    assert acc._followers == 200

def test_update_followers_to_zero():
    acc = InsAcc("user", 100, 10.0)
    acc.update_followers(0)
    assert acc._followers == 0

def test_update_followers_negative():
    acc = InsAcc("user", 100, 10.0)
    with pytest.raises(ValueError):
        acc.update_followers(-50)

def test_update_followers_wrong_type():
    acc = InsAcc("user", 100, 10.0)
    with pytest.raises(TypeError):
        acc.update_followers(150.5)

"""display() test"""
def test_base_display_not_implement():
    acc = InsAcc("aaa", 10, 10)
    result = acc.display()
    assert "Instagram Account" in result

"""get_engagement_stats() test"""
def test_base_get_engagement_stats():
    acc = InsAcc("aaa", 10, 10)
    stats = acc.get_engagement_stats()
    assert isinstance(stats, np.ndarray)

"""operator overloading test"""
def test_account_less_than_operator():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = InsAcc("bob", 200, 20.0)
    assert acc1 < acc2
    assert not (acc2 < acc1)

def test_account_less_than_case_insensitive():
    acc1 = InsAcc("Alice", 100, 10.0)
    acc2 = InsAcc("bob", 200, 20.0)
    assert acc1 < acc2

def test_account_less_than_wrong_type():
    acc = InsAcc("alice", 100, 10.0)
    with pytest.raises(TypeError):
        acc < "bob"

def test_account_equality_operator():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = FbAcc("alice", 200, 20.0)
    assert acc1 == acc2

def test_account_equality_case_insensitive():
    acc1 = InsAcc("Alice", 100, 10.0)
    acc2 = FbAcc("alice", 200, 20.0)
    assert acc1 == acc2

def test_account_equality_different_usernames():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = InsAcc("bob", 100, 10.0)
    assert not (acc1 == acc2)

def test_account_equality_wrong_type():
    acc = InsAcc("alice", 100, 10.0)
    assert not (acc == "alice")
    assert not (acc == 123)

def test_account_add_operator():
    acc = InsAcc("alice", 100, 10.0)
    result = acc + 5.0
    assert acc._avg_daily_minutes == 15.0
    assert result is acc

def test_account_add_operator_with_int():
    acc = InsAcc("alice", 100, 10.0)
    acc + 5
    assert acc._avg_daily_minutes == 15.0

#---instagram test---
"""constructor test"""
def test_ins_constructor():
    ig = InsAcc("eve", 200, 30.0)
    assert ig._username == "eve"
    assert ig._followers == 200
    assert ig._avg_daily_minutes == 30.0
    assert ig._post_likes == []
    assert ig._reel_views == []

"""add_post() test"""
def test_ins_add_post_valid():
    ig = InsAcc("eve", 200, 30)
    ig.add_post(50)
    assert ig._post_likes == [50]

def test_ins_add_post_negative():
    ig = InsAcc("eve", 200, 30)
    with pytest.raises(ValueError):
        ig.add_post(-1)

def test_ins_add_post_wrong_type():
    ig = InsAcc("eve", 200, 30)
    with pytest.raises(TypeError):
        ig.add_post(5.5)

def test_ins_add_multiple_posts():
    ig = InsAcc("user", 100, 10.0)
    ig.add_post(50)
    ig.add_post(100)
    ig.add_post(150)
    assert len(ig._post_likes) == 3

"""add_reel() test"""
def test_ins_add_reel_valid():
    ig = InsAcc("eve", 200, 30)
    ig.add_reel(300)
    assert ig._reel_views == [300]

def test_ins_add_reel_negative():
    ig = InsAcc("eve", 200, 30)
    with pytest.raises(ValueError):
        ig.add_reel(-20)

def test_ins_add_reel_wrong_type():
    ig = InsAcc("eve", 200, 30)
    with pytest.raises(TypeError):
        ig.add_reel("abc")

"""get_engagement_stats() test"""
def test_ins_stats_empty():
    ig = InsAcc("eve", 200, 30)
    stats = ig.get_engagement_stats()
    assert (stats == np.array([0.0, 0.0, 0.0])).all()

def test_ins_stats_filled():
    ig = InsAcc("eve", 200, 30)
    ig.add_post(10)
    ig.add_post(20)
    ig.add_reel(1000)
    stats = ig.get_engagement_stats()
    assert stats[0] == 2 #total post
    assert stats[1] == 15.0 #average likes: mean of 10 and 20
    assert stats[2] == 1000 #total reel views

"""display() test"""
def test_ins_display_contains_username():
    ig = InsAcc("eve", 200, 30)
    ig.add_post(10)
    ig.add_reel(50)
    result = ig.display()
    assert "Instagram Account: eve" in result
    assert "Followers: 200" in result
    assert "Avg Daily Minutes: 30" in result


#---facebook test---
"""constructor test"""
def test_fb_constructor():
    fb = FbAcc("bo", 100, 20)
    assert fb._post_reactions == []
    assert fb._groups == []

"""add_post() test"""
def test_fb_add_post_valid():
    fb = FbAcc("bo", 300, 40)
    fb.add_post(20)
    assert fb._post_reactions == [20]

def test_fb_add_post_negative():
    fb = FbAcc("bo", 300, 40)
    with pytest.raises(ValueError):
        fb.add_post(-10)

def test_fb_add_post_bad_type():
    fb = FbAcc("f", 10, 1)
    with pytest.raises(TypeError):
        fb.add_post(3.14)

def test_fb_add_multiple_posts():
    fb = FbAcc("user", 100, 10.0)
    fb.add_post(25)
    fb.add_post(50)
    fb.add_post(75)
    assert len(fb._post_reactions) == 3

"""join_group() test """
def test_fb_join_group_valid():
    fb = FbAcc("bo", 300, 40)
    fb.join_group("PSU Friends")
    assert fb._groups == ["PSU Friends"]

def test_fb_join_group_empty():
    fb = FbAcc("bo", 300, 40)
    with pytest.raises(ValueError):
        fb.join_group("")

def test_fb_join_group_bad_type():
    fb = FbAcc("f", 10, 1)
    with pytest.raises(TypeError):
        fb.join_group(123)

def test_fb_join_multiple_groups():
    fb = FbAcc("user", 100, 10.0)
    fb.join_group("Group1")
    fb.join_group("Group2")
    fb.join_group("Group3")
    assert len(fb._groups) == 3

"""get_engagement_stats() test"""
def test_fb_get_engagement_stats():
    fb = FbAcc("f", 10, 1)
    fb.add_post(10)
    fb.add_post(20)
    fb.join_group("A")
    fb.join_group("B")
    stats = fb.get_engagement_stats()
    assert stats[0] == 2 #number of posts
    assert stats[1] == 15.0 #average reactions
    assert stats[2] == 2   #number of groups

"""display() test"""
def test_fb_display():
    fb = FbAcc("bob", 100, 30)
    fb.add_post(10)
    fb.join_group("cars")
    result = fb.display()
    assert "Facebook Account: bob" in result
    assert "Followers: 100" in result


#----Tiktok test----
"""constructor test"""
def test_tiktok_constructor():
    tk = TiktokAcc("tt", 50, 10)
    assert tk._video_likes == []
    assert tk._shares == []

"""add_video() test"""
def test_tiktok_add_video_valid():
    tk = TiktokAcc("na", 150, 20)
    tk.add_video(500)
    assert tk._video_likes == [500]

def test_tiktok_add_video_negative():
    tk = TiktokAcc("na", 150, 20)
    with pytest.raises(ValueError):
        tk.add_video(-100)

def test_tiktok_add_video_bad_type():
    tk = TiktokAcc("t", 10, 5)
    with pytest.raises(TypeError):
        tk.add_video("abc")

def test_tiktok_add_multiple_videos():
    tk = TiktokAcc("user", 100, 10.0)
    tk.add_video(100)
    tk.add_video(200)
    tk.add_video(300)
    assert len(tk._video_likes) == 3

"""add_share() test"""
def test_tiktok_add_share_valid():
    tk = TiktokAcc("t", 10, 5)
    tk.add_share(30)
    assert tk._shares == [30]

def test_tiktok_add_share_bad_type():
    tk = TiktokAcc("t", 10, 5)
    with pytest.raises(TypeError):
        tk.add_share(3.14)

def test_tiktok_add_share_negative():
    tk = TiktokAcc("t", 10, 5)
    with pytest.raises(ValueError):
        tk.add_share(-10)

"""get_engagement_stats test"""
def test_tiktok_get_engagement_stats():
    tk = TiktokAcc("t", 10, 5)
    tk.add_video(10)
    tk.add_video(20)
    tk.add_share(5)
    stats = tk.get_engagement_stats()
    assert stats[0] == 2       # total videos
    assert stats[1] == 15.0    # average likes
    assert stats[2] == 5       # total shares

def test_tiktok_multiple_videos_avg_likes():
    tk = TiktokAcc("user", 100, 10.0)
    tk.add_video(100)
    tk.add_video(200)
    tk.add_video(300)
    stats = tk.get_engagement_stats()
    assert stats[1] == 200.0

"""display() test"""
def test_tiktok_display():
    tk = TiktokAcc("amy", 100, 20)
    tk.add_video(10)
    result = tk.display()
    assert "TikTok Account: amy" in result
    assert "Followers: 100" in result


#---RBTree Basic Operations---
"""insert() tests"""
def test_rbtree_insert_single():
    tree = RBTree()
    acc = InsAcc("alice", 100, 10.0)
    tree.insert(acc)
    assert len(tree) == 1
    assert tree.get_size() == 1

def test_rbtree_insert_multiple():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    tree.insert(FbAcc("bob", 200, 20.0))
    tree.insert(TiktokAcc("charlie", 300, 30.0))
    assert len(tree) == 3

def test_rbtree_insert_duplicate_raises_error():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    with pytest.raises(ValueError, match="Account already exist"):
        tree.insert(FbAcc("alice", 200, 20.0))

def test_rbtree_insert_case_insensitive_duplicate():
    tree = RBTree()
    tree.insert(InsAcc("Alice", 100, 10.0))
    with pytest.raises(ValueError):
        tree.insert(FbAcc("alice", 200, 20.0))

def test_rbtree_insert_non_account_raises_error():
    tree = RBTree()
    with pytest.raises(TypeError):
        tree.insert("not an account")

def test_rbtree_root_is_black():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    root = tree.get_root()
    assert root.get_color() == Color.BLACK

"""retrieve() tests"""
def test_rbtree_retrieve_existing():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    retrieved = tree.retrieve("alice")
    assert retrieved is not None
    assert retrieved.get_username() == "alice"

def test_rbtree_retrieve_nonexistent():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    retrieved = tree.retrieve("bob")
    assert retrieved is None

def test_rbtree_retrieve_case_insensitive():
    tree = RBTree()
    tree.insert(InsAcc("Alice", 100, 10.0))
    retrieved = tree.retrieve("alice")
    assert retrieved is not None
    assert retrieved.get_username() == "Alice"

def test_rbtree_retrieve_empty_string_raises_error():
    tree = RBTree()
    with pytest.raises(ValueError, match="username cannot be empty"):
        tree.retrieve("")

def test_rbtree_retrieve_non_string_raises_error():
    tree = RBTree()
    with pytest.raises(TypeError, match="username must be a string"):
        tree.retrieve(123)

"""display_all() tests"""
def test_rbtree_display_all_empty():
    tree = RBTree()
    displays = tree.display_all()
    assert displays == []

def test_rbtree_display_all_single():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    displays = tree.display_all()
    assert len(displays) == 1
    assert "alice" in displays[0]

def test_rbtree_display_all_sorted_order():
    tree = RBTree()
    tree.insert(InsAcc("charlie", 300, 30.0))
    tree.insert(InsAcc("alice", 100, 10.0))
    tree.insert(InsAcc("bob", 200, 20.0))
    displays = tree.display_all()
    assert len(displays) == 3
    assert "alice" in displays[0].lower()
    assert "bob" in displays[1].lower()
    assert "charlie" in displays[2].lower()

"""count_by_type() tests"""
def test_rbtree_count_by_type_empty():
    tree = RBTree()
    assert tree.count_by_type("Instagram") == 0

def test_rbtree_count_by_type_instagram():
    tree = RBTree()
    tree.insert(InsAcc("user1", 100, 10.0))
    tree.insert(FbAcc("user2", 200, 20.0))
    tree.insert(InsAcc("user3", 300, 30.0))
    assert tree.count_by_type("Instagram") == 2

def test_rbtree_count_by_type_facebook():
    tree = RBTree()
    tree.insert(FbAcc("user1", 100, 10.0))
    tree.insert(FbAcc("user2", 200, 20.0))
    tree.insert(TiktokAcc("user3", 300, 30.0))
    assert tree.count_by_type("Facebook") == 2

def test_rbtree_count_by_type_tiktok():
    tree = RBTree()
    tree.insert(TiktokAcc("user1", 100, 10.0))
    tree.insert(InsAcc("user2", 200, 20.0))
    tree.insert(TiktokAcc("user3", 300, 30.0))
    assert tree.count_by_type("TikTok") == 2

def test_rbtree_count_by_type_all_same():
    tree = RBTree()
    tree.insert(InsAcc("user1", 100, 10.0))
    tree.insert(InsAcc("user2", 200, 20.0))
    tree.insert(InsAcc("user3", 300, 30.0))
    assert tree.count_by_type("Instagram") == 3

"""get_total_followers() tests"""
def test_rbtree_total_followers_empty():
    tree = RBTree()
    assert tree.get_total_followers() == 0

def test_rbtree_total_followers_single():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    assert tree.get_total_followers() == 100

def test_rbtree_total_followers_multiple():
    tree = RBTree()
    tree.insert(InsAcc("user1", 100, 10.0))
    tree.insert(FbAcc("user2", 200, 20.0))
    tree.insert(TiktokAcc("user3", 300, 30.0))
    assert tree.get_total_followers() == 600

#---Operator Overloading Tests---
"""len() operator test"""
def test_rbtree_len_empty():
    tree = RBTree()
    assert len(tree) == 0

def test_rbtree_len_after_inserts():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    assert len(tree) == 1
    tree.insert(FbAcc("bob", 200, 20.0))
    assert len(tree) == 2

"""in operator test"""
def test_rbtree_contains_existing():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    assert "alice" in tree

def test_rbtree_contains_nonexistent():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    assert "bob" not in tree

def test_rbtree_contains_case_insensitive():
    tree = RBTree()
    tree.insert(InsAcc("Alice", 100, 10.0))
    assert "alice" in tree

def test_rbtree_contains_empty_tree():
    tree = RBTree()
    assert "alice" not in tree

def test_rbtree_contains_invalid_type():
    tree = RBTree()
    assert (123 in tree) == False

"""+= operator test"""
def test_rbtree_iadd_single():
    tree = RBTree()
    account = InsAcc("alice", 100, 10.0)
    tree += account
    assert len(tree) == 1

def test_rbtree_iadd_multiple():
    tree = RBTree()
    tree += InsAcc("alice", 100, 10.0)
    tree += FbAcc("bob", 200, 20.0)
    assert len(tree) == 2

def test_rbtree_iadd_returns_self():
    tree = RBTree()
    tree += InsAcc("alice", 100, 10.0)
    result = tree
    assert result is tree

#---Tree Structure Tests (Glass Box)---
"""Test tree structure after insertions"""
def test_rbtree_left_insertion():
    tree = RBTree()
    tree.insert(InsAcc("bob", 200, 20.0))
    tree.insert(InsAcc("alice", 100, 10.0))
    root = tree.get_root()
    assert root.get_left() is not None
    assert root.get_left().get_account().get_username() == "alice"

def test_rbtree_right_insertion():
    tree = RBTree()
    tree.insert(InsAcc("alice", 100, 10.0))
    tree.insert(InsAcc("bob", 200, 20.0))
    root = tree.get_root()
    assert root.get_right() is not None
    assert root.get_right().get_account().get_username() == "bob"

def test_rbtree_complex_structure():
    tree = RBTree()
    usernames = ["dog", "cat", "elephant", "ant", "bear", "fox"]
    for name in usernames:
        tree.insert(InsAcc(name, 100, 10.0))
    
    assert len(tree) == 6
    assert tree.get_root().get_color() == Color.BLACK
    
    # verify all can be retrieved
    for name in usernames:
        assert tree.retrieve(name) is not None

#---Node Class Tests---
"""Node constructor tests"""
def test_node_constructor_valid():
    acc = InsAcc("alice", 100, 10.0)
    node = Node(acc)
    assert node.get_account() == acc
    assert node.get_color() == Color.RED
    assert node.get_left() is None
    assert node.get_right() is None
    assert node.get_parent() is None

def test_node_constructor_invalid_type():
    with pytest.raises(TypeError):
        Node("not an account")

"""Node setter/getter tests"""
def test_node_set_color():
    acc = InsAcc("alice", 100, 10.0)
    node = Node(acc)
    node.set_color(Color.BLACK)
    assert node.get_color() == Color.BLACK

def test_node_set_color_invalid():
    acc = InsAcc("alice", 100, 10.0)
    node = Node(acc)
    with pytest.raises(TypeError):
        node.set_color("red")

def test_node_set_left():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = InsAcc("bob", 200, 20.0)
    node1 = Node(acc1)
    node2 = Node(acc2)
    node1.set_left(node2)
    assert node1.get_left() == node2

def test_node_set_right():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = InsAcc("bob", 200, 20.0)
    node1 = Node(acc1)
    node2 = Node(acc2)
    node1.set_right(node2)
    assert node1.get_right() == node2

def test_node_set_parent():
    acc1 = InsAcc("alice", 100, 10.0)
    acc2 = InsAcc("bob", 200, 20.0)
    node1 = Node(acc1)
    node2 = Node(acc2)
    node2.set_parent(node1)
    assert node2.get_parent() == node1

#---Integration Tests---
"""Test complete workflows"""
def test_integration_add_retrieve_modify():
    tree = RBTree()
    
    # add instagram account
    ins = InsAcc("alice", 1000, 30.0)
    ins.add_post(100)
    ins.add_reel(500)
    tree.insert(ins)
    
    # add facebook account
    fb = FbAcc("bob", 500, 20.0)
    fb.add_post(50)
    fb.join_group("Test Group")
    tree.insert(fb)
    
    # retrieve and modify
    retrieved = tree.retrieve("alice")
    assert retrieved is not None
    retrieved.record_session(10.0)
    assert retrieved.get_avg_daily_minutes() == 40.0
    
    # verify statistics
    assert tree.get_total_followers() == 1500
    assert len(tree) == 2
    assert tree.count_by_type("Instagram") == 1
    assert tree.count_by_type("Facebook") == 1

def test_integration_all_three_types():
    tree = RBTree()
    
    # add all three types
    tree += InsAcc("alice", 100, 10.0)
    tree += FbAcc("bob", 200, 20.0)
    tree += TiktokAcc("charlie", 300, 30.0)
    
    # verify counts
    assert tree.count_by_type("Instagram") == 1
    assert tree.count_by_type("Facebook") == 1
    assert tree.count_by_type("TikTok") == 1
    
    # verify total
    assert tree.get_total_followers() == 600
    
    # verify sorted display
    displays = tree.display_all()
    assert len(displays) == 3

def test_integration_operator_overloading():
    tree = RBTree()
    
    # use += to add
    tree += InsAcc("alice", 100, 10.0)
    tree += FbAcc("bob", 200, 20.0)
    
    # use len()
    assert len(tree) == 2
    
    # use in
    assert "alice" in tree
    assert "charlie" not in tree
    
    # retrieve and use + operator on account
    acc = tree.retrieve("alice")
    acc + 5.0
    assert acc.get_avg_daily_minutes() == 15.0