# Taiwan ID Validator  
  
## Disclaimer
The following content is for educational purposes only.  
Do not use it for illegal activities.  
It might takes much time.  
  
## Validation  
According to [Wikipedia](https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%B0%91%E8%BA%AB%E5%88%86%E8%AD%89#%E9%A9%97%E8%AD%89%E8%A6%8F%E5%89%87),  
the first English letter represents the birthplace ([wiki](https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%B0%91%E8%BA%AB%E5%88%86%E8%AD%89#%E7%B7%A8%E8%99%9F%E8%A6%8F%E5%89%87)),  
the following number indicates the person's gender,  
the third number is the identity,  
and the remaining numbers construct a valid ID with the previous conponents.  

The First English letter is translated into a two-digit integer ([wiki](https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%B0%91%E8%BA%AB%E5%88%86%E8%AD%89#%E7%B7%A8%E8%99%9F%E8%A6%8F%E5%89%87)), thus the ID will become a 11-digit intger.  
Take each digit multiplies `19876543211` respectively, and divide the result.  
If the remainder is zero, then this is a valid ID.  

## To-Do

- [x] the third number
- [ ] foreigners
- [ ] GUI
- [ ] refactoring
- [x] separate main and functions