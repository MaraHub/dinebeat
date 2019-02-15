/**
 * Custom JS
 * Use this file to add your custom scripts
 */

  // $(document).ready(function(){
  //   $(".section_menu__item").click(function(){
  //     $(this).fadeOut( "slow",0.5,function(){} );
  //   });
  // });

  // $( ".section_menu__item" ).click(function() {
  //   $( this ).fadeTo( "slow", 0.33 );
  // });

  // $(".section_menu__item").toggle(
  // function() {
  //
  //     $(this).fadeTo( "slow", 0.33 );
  // },
  // function() {
  //
  //   $(this).fadeIn( "slow");
  // });

      // $(".section_menu__item").click(function () {
      //     $(this).toggle = !$(this).toggle;
      //     $(".section_menu__item").stop().fadeTo(400, this.toggle ? 0.4 : 1);
      // });

// General Use Functions
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};
//var tech = getUrlParameter('technology');

$("#submit_menu_confirmation_b").click(function(){

  window.history.back();
});



      $( ".section_menu__item" ).click(function() {
        $(this).toggleClass('section_menu__item section_menu__item_selected')
      });

      // $( "h4" ).each(function( index ) {
      //   console.log( index + ": " + $( this ).text() );
      // });

      function put_to_array( divs ) {
        var a = [];
        for ( var i = 0; i < divs.length; i++ ) {
          console.log(divs[ i ].innerHTML );
          a.push(divs[ i ].innerHTML)
        } return a;
      }

//Remember here you need to change the below funcion to add names for different courses(starters,mains) to get
// the da with the ither function ex. name=piato_main kai name=perigrafh_main name=piato_starter kai perigrafh_starter

      $("#add_item_starter").click(function (){
        var menuitem = '<br><div class="row"><div class="col"><input type="text" class="form-control" name="dish_starter" placeholder="Πιάτο"></div><div class="col"><input type="text" class="form-control" name="desc_starter" placeholder="Περιγραφή Πιάτου"></div></div>';
          $('#submit_menu_form_starter').append($(menuitem));
      });

      $("#add_item_main").click(function (){
        var menuitem = '<br><div class="row"><div class="col"><input type="text" class="form-control" name="dish_main" placeholder="Πιάτο"></div><div class="col"><input type="text" class="form-control" name="desc_main" placeholder="Περιγραφή Πιάτου"></div></div>';
          $('#submit_menu_form_main').append($(menuitem));
      });

  $("#add_item_desserts").click(function (){
        var menuitem = '<br><div class="row"><div class="col"><input type="text" class="form-control" name="dish_desserts" placeholder="Πιάτο"></div><div class="col"><input type="text" class="form-control" name="desc_desserts" placeholder="Περιγραφή Πιάτου"></div></div>';
          $('#submit_menu_form_desserts').append($(menuitem));
      });

  $("#add_item_drinks").click(function (){
        var menuitem = '<br><div class="row"><div class="col"><input type="text" class="form-control" name="drinks" placeholder="Πιάτο"></div><div class="col"><input type="text" class="form-control" name="desc_drinks" placeholder="Περιγραφή Πιάτου"></div></div>';
          $('#submit_menu_form_drinks').append($(menuitem));
      });











  $(function() {
        $("#submit_menu_guest").click( function()
             {

               // alert('button clicked');
               var numselections = $('.section_menu__item_selected .entree').length;
               var selections = $(".section_menu__item_selected .desserts").toArray();
                var entree = $(".section_menu__item_selected .entree").toArray();
                var kyriws = $(".section_menu__item_selected .kyriws").toArray();
                var desserts = $(".section_menu__item_selected .desserts").toArray();
                var drinks = $(".section_menu__item_selected .drinks").toArray();

               //var test = $('.section_menu__item_selected').serialize();
               //var cars = JSON.stringify(put_to_array(selections));
               //console.log(put_to_array(selections).length);
               //console.log(typeof $(".section_menu__item_selected piato"));

               $.ajax({

                  url: '/post_menu_voted',
                  type: 'POST',
                  dataType: 'json',
                  data:{
                         // 'event_code':getUrlParameter('event_code_id') ,
                         'starters': JSON.stringify(put_to_array(entree)),
                         'main': JSON.stringify(put_to_array(kyriws)),
                         'desserts': JSON.stringify(put_to_array(desserts)),
                         'drinks': JSON.stringify(put_to_array(drinks))
                        // ,'voter':getUrlParameter('voter_name')
                      },
                      success:function(response)
                                    {
                                      if (response.redirect) {
                                        window.location.href = response.redirect;
                                    }
                                  }
                      });

               if (numselections>1){
                 console.log('Please select less than 2');
               }

             }
        );
  });






  $(function() {
        $("#submit_menu_company").click( function()
             {

               // alert('button clicked');

            //    var entree = $("#submit_menu_form_starter").toArray();
                 var dish_starter = $('[name="dish_starter"]').serializeArray();
                 var desc_starter = $('[name="desc_starter"]').serializeArray();
                 var dish_main = $('[name="dish_main"]').serializeArray();
                 var desc_main = $('[name="desc_main"]').serializeArray();
                 var dish_desserts = $('[name="dish_desserts"]').serializeArray();
	               var desc_desserts = $('[name="desc_desserts"]').serializeArray();
                 var drinks = $('[name="drinks"]').serializeArray();
                  var desc_drinks = $('[name="desc_drinks"]').serializeArray();

                console.log(dish_starter.length);


               $.ajax({

                  url: '/receiver2',
                  type: 'POST',
                  dataType: 'json',
                  data:{ 'dish_starter': JSON.stringify(dish_starter),
                  'desc_starter': JSON.stringify(desc_starter),
                  'dish_main': JSON.stringify(dish_main),
                  'desc_main': JSON.stringify(desc_main),
                  'dish_desserts': JSON.stringify(dish_desserts),
                  'desc_desserts': JSON.stringify(desc_desserts),
 		               'drinks': JSON.stringify(drinks),
                   'desc_drinks': JSON.stringify(desc_drinks)



                      },
                      //This is where you say to the funciton to redirect to page
                  success:function(response)
                                {
                                  if (response.redirect) {
                                    window.location.href = response.redirect;
                                }
                              }
                      });



               if (dish_starter.length>1){
                 console.log('Please select less than 2');
               }

             }
        );
  });
