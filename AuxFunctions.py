

## Function to join the page ID with the product ID to generate a unique product ID
  
def product_code(num1, num2):
  return int("{}{}".format(num1, num2))




## Function to TRY and Extract the individual data from each product in the Page being scraped
        
def extract_data(product, selector):
  try:
    return product.select_one(selector).text
  except AttributeError:
    return None
  
  
  
  
## Function for the Product Link 
  
def product_link(item, selector, class_):
    
    try:
        #return item.find(selector, href=True)['href']
        return item.find(selector, {'class':class_}).get('href')
    
    except AttributeError:
        return None

      
## Function for the Product Image 
  
def product_image(item, selector):
    
    try:
        return item.find(selector, srcset=True)['srcset']
    
    except TypeError:
        return None
      
      
## Function for Labels 
  
def labels(item, selector, class_):
  
  label_list = []
    
  try:
      return item.find_all(selector, {'class':class_}).get('title')
          
        #label_list.append(label)
          
        #return label_list
          
      
    
  except AttributeError:
    return None
      
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on M&amp;S Taste Match"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/M-S-Taste-Match-Icon?$Icon-wapp2x$=&amp;qlt=50"><img alt="M&amp;S Taste Match" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/M-S-Taste-Match-Icon?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="M&amp;S Taste Match"></picture></button></div></li>
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on Typically fresh for 2 days"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/produce-2-days-icon?$Icon-wapp2x$=&amp;qlt=50"><img alt="Typically fresh for 2 days" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/produce-2-days-icon?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="Typically fresh for 2 days"></picture></button></div></li>
#<li class="co-product__promo-icon-item"><div class="co-product__promo-icon-image-cntr"><button data-auto-id="btnPromo" type="button" class="asda-btn asda-btn--plain co-product__promo-icon-button" aria-label="show information on Live Better"><picture class="asda-image picture"><source srcset="https://ui.assets-asda.com/dm/_923_LiveBetter_Update?$Icon-wapp2x$=&amp;qlt=50"><img alt="Live Better" class="asda-img asda-image co-product__promo-icon-img" data-auto-id="" src="https://ui.assets-asda.com/dm/_923_LiveBetter_Update?$Icon-wapp2x$=&amp;qlt=50" loading="lazy" title="Live Better"></picture></button></div></li>
        