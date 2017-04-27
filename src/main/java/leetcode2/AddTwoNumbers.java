package leetcode2;

import org.junit.Test;

/**
 * Created by wubo on 2017-4-25.
 */
public class AddTwoNumbers {

    @Test
    public void testRun(){
        ListNode l1 = new ListNode(9);
        l1.next = new ListNode(1);
        l1.next.next = new ListNode(6);
//        l1.next.next.next = new ListNode(3);

        ListNode l2 = new ListNode(0);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        ListNode result = addTwoNumbers(l1,l2);
        while(result!=null){
            System.out.print(result.val);
            result = result.next;
        }
    }

    /**
     Definition for singly-linked list.
     */
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }    /**
     *
     You are given two non-empty linked lists representing two non-negative integers.
     The digits are stored in reverse order and each of their nodes contain a single digit.
     Add the two numbers and return it as a linked list.
     You may assume the two numbers do not contain any leading zero, except the number 0 itself.

     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
     Output: 7 -> 0 -> 8

     */


    /**
     *  Own method
     *  O n
     * @param l1
     * @param l2
     * @return
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode result = new ListNode(0);
        ListNode listNode = result;
        int emp =0;
        //处理长度相同的部分
        while(l1!=null && l2!=null){
            listNode.val = l1.val + l2.val + emp;
            emp=0;
            if(listNode.val>9){
                emp = listNode.val/10;
                listNode.val = 0;
            }
            l1=l1.next;l2=l2.next;
            if(l1!=null || l2!=null) {
                listNode.next = new ListNode(0);
                listNode = listNode.next;
            }
        }
        //处理长度不同的情况
        while(l1!=null){
            listNode.val = emp + l1.val;
            if(listNode.val>9){
                emp = listNode.val/10;
                listNode.val = 0;
            }
            l1=l1.next;
            if(l1!=null) {
                listNode.next = new ListNode(0);
                listNode = listNode.next;
            }
        }
        while(l2!=null){
            listNode.val = emp + l2.val;
            if(listNode.val>9){
                emp = listNode.val/10;
                listNode.val = 0;
            }
            l2=l2.next;
            if(l2!=null) {
                listNode.next = new ListNode(0);
                listNode = listNode.next;
            }
        }
        //收尾 看看前面计算有没有产生进位的
        if(emp!=0){
            listNode.next = new ListNode(1);
        }
        return result;
    }
}
