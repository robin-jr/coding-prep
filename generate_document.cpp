#include <bits/stdc++.h>

using namespace std;

bool generateDocument(string characters, string document) {
  map<char, int> characters_map={};
  map<char, int> document_map={};
  for (auto &&i : characters)
  {
      characters_map[i]+=1;
  }

  for (auto &&i : document)
  {
      document_map[i]+=1;
  }

  for (auto &&i : document_map)
  {
   char k = i.first;
   int v=i.second;
    if (characters_map[k]<v)
    {
        return false;
    }
  }
 return true; 
}

int main(){
   string characters="Bstehetsi ogEAxpelrt x ";
   string document="AlgoExpert is the Best!" ;
   bool x = generateDocument(characters, document);
   cout<<x;
}
