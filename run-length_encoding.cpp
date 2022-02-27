#include <bits/stdc++.h>

using namespace std;

void addCode(vector<char>& s,int counter,char c){
  while (counter>9)
  {
    s.push_back('9');
    s.push_back(c);
    counter-=9;
  }
  if(counter>0){
      s.push_back(to_string(counter)[0]);
      s.push_back(c);
  }
}

string runLengthEncoding(string str) {
  int counter=1;
  vector<char> s;
  int n = str.size();
  
  for (int i = 1; i < n; i++)
  {
     if(str[i]==str[i-1]){
       counter += 1;
     }else{
       addCode(s,counter,str[i-1]);
       counter=1;
     }
  }
  addCode(s,counter,str[n-1]);
  return string(s.begin(),s.end());
}


int main(){
    string a="a";
    string x=runLengthEncoding(a);
    cout<<x;
}