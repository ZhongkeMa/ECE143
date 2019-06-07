# [LRU Cache][title]

## Description

Design and implement a data structure for [Least Recently Used (LRU)
cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It
should support the following operations: `get` and `put`.

`get(key)` \- Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.  
`put(key, value)` \- Set or insert the value if the key is not already
present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Follow up:**  
Could you do both operations in **O(1)** time complexity?

**Example:**
        




**Tags:** Design

**Difficulty:** Hard

## 思路

``` cpp
class LRUCache {
public:
    unordered_map<int,list<pair<int,int>>::iterator> cache;
    list<pair<int,int>> holder;
    int capacity;
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if(cache.find(key) == cache.end())
            return -1;
        else {
            holder.splice(holder.begin(), holder, cache[key]);
            return cache[key]->second;
        }
        
    }
    
    void put(int key, int value) {
        if(cache.find(key) == cache.end()) {
            if(cache.size() == capacity) {
                cache.erase(holder.back().first);
                holder.pop_back();
            }
            holder.push_front(make_pair(key,value));
            cache[key] = holder.begin();
        }
        else {
            cache[key]->second = value;
            holder.splice(holder.begin(), holder, cache[key]);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

[title]: https://leetcode.com/problems/lru-cache