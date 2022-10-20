package com.company;

public class RemoveDuplicateWords {

    public static String removeDuplicateWords(String s){

        String[] str = s.split(" ");
        String result = "";
        boolean isDuplicate = false;
        for(int i=0; i<str.length; i++){
            for(int j=i+1; j<str.length; j++){
                if(str[i].equals(str[j])){
                 isDuplicate = true;
                 break;
                }
            }
            if(!isDuplicate){
                result += str[i] + " ";
            }
            isDuplicate = false;
        }
        return result.trim();
    }
}
