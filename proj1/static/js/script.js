var container = document.getElementById('container')
var slider = document.getElementById('slider');
console.log(slider)
var slides = document.getElementsByClassName('slide').length;
var buttons = document.getElementsByClassName('btn');


var currentPosition = 0;
var currentMargin = 0;
var slidesPerPage = 0;
var slidesCount = slides - slidesPerPage;
// var containerWidth = container.offsetWidth;
var prevKeyActive = false;
var nextKeyActive = true;

window.addEventListener("resize", checkWidth);

function checkWidth() {
    // containerWidth = container.offsetWidth;
    // setParams(containerWidth);
}

function add_to_cart_slug(prod_id){
    $.ajax({
        method : "GET",
        url : `/add-to-cart-slug/${prod_id}/`,
        data : {},
        success : function(data){
            console.log(data)
            if(data.success){
                showMessage("success", "Product added to Cart successfully!")
            }
        },
        error : function(error){
            console.log(error)
        }
    })
}
let addToCart_btns = document.querySelectorAll(".addToCart");
for (let index = 0; index < addToCart_btns.length; index++) {
    let element = addToCart_btns[index];
    element.addEventListener("click",function(e) {
        console.log(element)
        console.log(element.getAttribute("pid"))
      add_to_cart_slug(element.getAttribute("pid"))  
    })
    
}

function showMessage(type, msg){
    let alert = document.querySelectorAll('.alert')[0];
    if(alert.classList.contains("d-none")){
        alert.classList.remove("d-none");
    }
    if(type === "success"){
        alert.classList.add("alert-success");
    }
    alert.children[0].innerHTML = msg;
    setTimeout(() => {
        hideMessage()
    }, 3000);
}

function hideMessage(){
    let alert = document.querySelectorAll('.alert')[0];
    console.log(alert)
    
    if(!alert.classList.contains("d-none")){
        alert.classList.add("d-none");
    }

}

var emptyCartImage = document.getElementById("emptyCartImage");
$('.remove-cart').click(function () {
    var $this = $(this); // Capture the value of $(this)
    remove_cart_func($this); // Pass $this to the function
});

function remove_cart_func(element) {
    showLoading()
    let id
    try {
        id = element.closest('.justify-content-end').querySelector('.remove-cart').getAttribute('pid');
    } catch (error) {
        id = element.closest('.justify-content-end').find(".remove-cart").attr('pid');
    }
    showLoading()
    $.ajax(
        {
            type: "GET",
            url: "/remove-cart/",
            data: {
                prod_id: id
            },
            success: function (data) {
                if (data.success) {
                    hideLoading()
                    // document.getElementById("total_items").innerHTML = data.cart_items;
                    document.querySelector(".checkOut-btn").children[0].innerText = data.totalamount;

                    element.closest('.cartItem').remove()
                    if (data.cart_items === 0) {
                        if (empty_cart_section.classList.contains("d-none")) {
                            empty_cart_section.classList.remove("d-none")
                            empty_cart_section.classList.add("d-flex")
                        }
                        if (cart_items_section) {
                            if (!cart_items_section.classList.contains("d-none")) {
                                cart_items_section.classList.add("d-none")
                            }
                        }
                    }
                }
                else if (data.error === "auth_error") {
                    hideLoading()
                    window.location.href = "/login/"
                }
                else {
                    hideLoading()
                    alert("Something went wrong")
                }
            }
        })
};
$('.plus-cart').click(function () {
    let id;
        id = element.closest('.input-group').querySelector('.plus-cart').getAttribute('pid');
        console.log(id)
    
    $.ajax(
        {
            type: "GET",
            url: "/plus-cart/",
            data: {
                prod_id: id,
            },
            success: function (data) {
                console.log(data)
                try {
                    element.closest(".qty-container").find('input').val(data.quantity);
                    element.closest(".cartItem").find(".cart_product_discounted_price").text(data.amount);
                } catch (error) {
                    element.closest(".qty-container").querySelector('input').value = data.quantity;
                    element.closest(".cartItem").querySelector("span").querySelector("span").innerText = data.amount;
                }
                document.querySelector(".checkOut-btn").children[0].innerText = data.totalamount;
            }
        }) 
    });
$('.minus-cart').click(function () {
    var $this = $(this); // Capture the value of $(this)
    minus_cart_func($this); // Pass $this to the function
    $.ajax(
        {
            type: "GET",
            url: "/minus-cart/",
            data: {
                prod_id: id
            },
            success: function (data) {
                hideLoading()
                try {
                    element.closest(".qty-container").find('input').val(data.quantity);
                    element.closest(".cartItem").find(".cart_product_discounted_price").text(data.amount);
                } catch (error) {
                    element.closest(".qty-container").querySelector('input').value = data.quantity;
                    element.closest(".cartItem").querySelector("span").querySelector("span").innerText = data.amount;
                }
                // eml.parentNode.parentNode.parentNode.parentNode.children[1].children[1].children[0]
                // document.getElementById("subtotal").innerText = data.totalamount;
                document.querySelector(".checkOut-btn").children[0].innerText = data.totalamount;
            }
        })
    });

let cart_items_section = document.getElementById("cart-items-section")
let empty_cart_section = document.getElementById("empty-cart-section")
if (document.getElementsByClassName("cartItem").length > 0) {
    if (!empty_cart_section.classList.contains("d-none")) {
        empty_cart_section.classList.add("d-none")
        empty_cart_section.classList.remove("d-flex")
    }

    if (cart_items_section.classList.contains("d-none")) {
        cart_items_section.classList.remove("d-none")
    }
}
else if (document.getElementsByClassName("cartItem").length === 0) {

    if (empty_cart_section) {
        if ((empty_cart_section.classList.contains("d-none"))) {
            empty_cart_section.classList.remove("d-none")
            empty_cart_section.classList.add("d-flex")
        }
    }
    if (cart_items_section) {
        if (!cart_items_section.classList.contains("d-none")) {
            cart_items_section.classList.add("d-none")
        }
    }

}

function setParams(w) {
    if (w < 551) {
        slidesPerPage = 1;
    } else {
        if (w < 901) {
            slidesPerPage = 2;
        } else {
            if (w < 1101) {
                slidesPerPage = 3;
            } else {
                slidesPerPage = 4;
            }
        }
    }
    slidesCount = slides - slidesPerPage;
    if (currentPosition > slidesCount) {
        currentPosition -= slidesPerPage;
    };
    currentMargin = - currentPosition * (100 / slidesPerPage);
    // slider.style.marginLeft = currentMargin + '%';
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
    if (currentPosition < slidesCount) {
        // buttons[1].classList.remove('inactive');
    }
    if (currentPosition >= slidesCount) {
        buttons[1].classList.add('inactive');
    }
}

setParams();

function slideRight() {
    if (currentPosition != 0) {
        slider.style.marginLeft = currentMargin + (100 / slidesPerPage) + '%';
        currentMargin += (100 / slidesPerPage);
        currentPosition--;
    };
    if (currentPosition === 0) {
        buttons[0].classList.add('inactive');
    }
    if (currentPosition < slidesCount) {
        buttons[1].classList.remove('inactive');
    }
};

function slideLeft() {
    if (currentPosition != slidesCount) {
        slider.style.marginLeft = currentMargin - (100 / slidesPerPage) + '%';
        currentMargin -= (100 / slidesPerPage);
        currentPosition++;
    };
    if (currentPosition == slidesCount) {
        buttons[1].classList.add('inactive');
    }
    if (currentPosition > 0) {
        buttons[0].classList.remove('inactive');
    }
};






    // Get references to the button and menu
    var toggleButton = document.querySelector('.toggle');
    var menu = document.querySelector('.right-nav');

    // Add click event listener to the button
    function togglemenu() {
        // Toggle the menu's visibility
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
            // Remove the 'active' class when hiding the menu
            menu.classList.remove('active');
        } else {
            menu.style.display = 'block';
            // Add the 'active' class when showing the menu
            menu.classList.add('active');
        }
    };

    var cart = document.querySelector('.cart');
    var cartmenu = document.querySelector('.left-nav');

    // Add click event listener to the button
    function cartbtn() {
        // Toggle the cartmenu's visibility
        if (cartmenu.style.display === 'block') {
            cartmenu.style.display = 'none';
            // Remove the 'active' class when hiding the cartmenu
            cartmenu.classList.remove('active');
        } else {
            cartmenu.style.display = 'block';
            // Add the 'active' class when showing the cartmenu
            cartmenu.classList.add('active');
        }
    };

   
  