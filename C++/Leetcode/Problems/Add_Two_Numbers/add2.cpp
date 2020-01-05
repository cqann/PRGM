
#include <iostream>
#include <cmath>
#include <math.h>
#include <time.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm> 

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *node1 = l1;
        ListNode *node2 = l2;
        int carry = 0;
        

        while (!(node1 == NULL && node2 == NULL)){
            int v_from_1 = (node1 == NULL) ? 0 : node1->val;
            int v_from_2 = node2->val;
            int new_val = v_from_1 + v_from_2 + carry;
            carry = (new_val != 0) ? floor(log10(new_val)) : 0;
            new_val -= 10*carry;
            node2->val = new_val;
            bool check = ((node1 == NULL) ? false : node1->next != NULL);
            if (node2->next == NULL){
                if(carry != 0 || check){
                    ListNode *to_add;
                    node2->next = new ListNode(0);
                }  
            }
            if (node1 != NULL) node1 = node1->next;
            node2 = node2->next;
            
        }
        

        return l2;

    }
};




int main()
{
    clock_t tStart = clock();

    ListNode l1(0);
    
    

    ListNode s1(0);
    

    Solution sol;
    ListNode *cur = sol.addTwoNumbers(&l1,&s1);
    while (cur != NULL){
        cout << cur->val;
        cur = cur->next;
    } 
     

    
    
    printf("\nTime taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}


/*
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        long long l1_sum = 0;
        long long l2_sum = 0;
        ListNode *cur_node = l1;
        int i = 0;

        while (cur_node != NULL) {
            l1_sum += cur_node->val * pow(10,i);
            i++;
            cur_node = cur_node->next;
        } 

        cur_node = l2;
        i = 0;


        while (cur_node!= NULL) {
            l2_sum += cur_node->val * pow(10,i);
            i++;
            cur_node = cur_node->next;
        } 

        long long l1_add_l2 = l1_sum + l2_sum;
        string sum_str = to_string(l1_add_l2);
        ListNode *newNode;
        newNode = new ListNode(sum_str[sum_str.size()-1]-'0');
        ListNode *prev = newNode;
        ListNode *to_add;
        for (int k = sum_str.size()-2; k >= 0; k--){
            to_add = new ListNode(sum_str[k]-'0');
            prev->next = to_add;
            prev = to_add;
        }
        

        return newNode;

    }
};
*/