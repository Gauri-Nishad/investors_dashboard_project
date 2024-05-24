function showMessage(elementId, message) {
  document.getElementById(elementId).innerText = message;
  setTimeout(function () {
      document.getElementById(elementId).innerText = "";
  }, 3000); 
}

// function submitFunction() {

  // var name = document.getElementById('name').value;
  // var email = document.getElementById('email').value;
  // var role = document.getElementById('role').value;
  // var mobile = document.getElementById('mobile').value;
  // var password=document.getElementById('password').value;
   
  
  // var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  // if (name == "") {
  //     showMessage('nameMessage', 'Name is required');
  //     return false;
  // }


  // if(email==""){
  //     showMessage('emailMessage','Email is requred');
  //     return false;
  // }
  // else if(!email.match(validRegex)){
  //     showMessage('emailMessage','Please enter a valid email');
  //     return false;
  // }
//   if(role=="Select Role"){
//     showMessage('roleMessage','Please select role');
//     return false;
// }
   
  // if(mobile==""){
  //     showMessage('mobileMessage','Mobile number is requred');
  //     return false;
  // }
  // else if(mobile.length !==10){
  //     showMessage('mobileMessage','Mobile number must be 10 digit');
  //     return false;
  // }

  
//   if (password==""){
//     showMessage('passwordMessage','Please Enter Password')
//     return false;
//    } 
// }

function loginbutton(){
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;

  if (email == "") {
    showMessage('emailMessage', 'Email is required');
    return false;
  }

  else if(!email.match(validRegex)){
  showMessage('emailMessage','Please enter a valid email');
  return false;
   }

if (password == "") {
  showMessage('passwordMessage', 'Password is required');
  return false;
}

}

function submitbuttonemail(){
  var email = document.getElementById('email').value;
 

  var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;

  if (email == "") {
    showMessage('emailMessage', 'Please enter an email');
    return false;
  }

  else if(!email.match(validRegex)){
  showMessage('emailMessage','Please enter a valid email');
  return false;
   }
  }

  function submitbuttonreset(){
    var password1 = document.getElementById('new_password').value;
    var password2 = document.getElementById('confirm_password').value;

    if(password1==""){
      showMessage('passwordMessage1','Please enter a password');
      return false;
    }
    if(password2==""){
      showMessage('passwordMessage2','Please re-enter a password');
      return false;
    }

  }

$(document).ready(function() {
  
  setTimeout(function() {
      $('.message1').fadeOut('slow');
  }, 2000); 
});

function truncateInputValue(inputElement) {
  if (inputElement.value.length > 10) {
      inputElement.value = inputElement.value.slice(0, 10);
  }
}

$(document).ready(function() {
    $(".txtOnly").keypress(function(e) {
        var key = e.which;
         
        if (!((key >= 65 && key <= 90) || (key >= 97 && key <= 122))) {
            e.preventDefault();
        }
    });
});


// function rolevalidation(){
//   var name = document.getElementById('name').value;
//   name.trim();
//   if (name == "") {
//     showMessage('nameMessage', 'Role name  is required');
//     return false;
//   }
// }


// function roleupdatevalidation(){
 
//   var name = document.getElementById('name1').value;
//   name.trim();
   
//   if (name == "") {
//     showMessage('nameMessage1', 'Role name  is required');
//     return false;
//   }
// }

// function submituserupdate() {

//   var name = document.getElementById('name1').value;
//   var email = document.getElementById('email1').value;
//   var role = document.getElementById('role1').value;
//   var mobile = document.getElementById('mobile1').value;
   
   
  
//   var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if (name == "") {
//       showMessage('nameMessage1', 'Name is required');
      
//       return false;
      
//   }

  // if(email==""){
  //     showMessage('emailMessage1','Email is requred');
      
  //     return false;
  // }
  // else if(!email.match(validRegex)){
  //     showMessage('emailMessage1','Please enter a valid email');
      
  //     return false;
  // }
//   if(role=="Select Role"){
//     showMessage('roleMessage1','Please select role');
//     return false;
// }
   
//   if(mobile==""){
//       showMessage('mobileMessage1','Mobile number is requred');
      
//       return false;
//   }
  // else if(mobile.length !==10){
  //     showMessage('mobileMessage1','Mobile number must be 10 digit');
       
  //     return false;
  // }

   
// }


// function submitFn() {
//   console.log('function is called')
//   var first_name = document.getElementById('first_name').value;
//   var last_name = document.getElementById('last_name').value;
//   var email = document.getElementById('email').value;
 
//   var mobile = document.getElementById('mobile').value;
  
   
  
 
//   if (first_name == "") {
//       showMessage('first_nameMessage1', 'First Name is required');
//       return false;
//   }
//   if (last_name == "") {
//     showMessage('last_nameMessage1', 'Last Name is required');
//     return false;
// }

   
 
// var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if(email==""){
//       showMessage('emailMessage1','Email is requred');
//       return false;
//   }
//   // else if(!email.match(validRegex)){
//   //     showMessage('emailMessage1','Please enter a valid email');
//   //     return false;
//   // }
  
   
//   if(mobile==""){
//       showMessage('mobileMessage1','Mobile number is requred');
//       return false;
//   }
//   // else if(mobile.length !==10){
//   //     showMessage('mobileMessage1','Mobile number must be 10 digit');
//   //     return false;
//   // }

  
// }



// function submitinvestor() {
//   console.log('function is called')
//   var first_name = document.getElementById('first_name1').value;
//   var last_name = document.getElementById('last_name1').value;
//   var email = document.getElementById('email1').value;
 
//   var mobile = document.getElementById('mobile1').value;
  
   
  
 
//   if (first_name == "") {
//       showMessage('first_nameMessage', 'First Name is required');
//       return false;
//   }
//   if (last_name == "") {
//     showMessage('last_nameMessage', 'Last Name is required');
//     return false;
// }

   
 
// var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if(email==""){
//       showMessage('emailMessage','Email is requred');
//       return false;
//   }
//   else if(!email.match(validRegex)){
//       showMessage('emailMessage','Please enter a valid email');
//       return false;
//   }
  
   
//   if(mobile==""){
//       showMessage('mobileMessage','Mobile number is requred');
//       return false;
//   }
//   else if(mobile.length !==10){
//       showMessage('mobileMessage','Mobile number must be 10 digit');
//       return false;
//   }

  
// }




// function submitFn() {
//   console.log('function is called')
//   var first_name = document.getElementById('first_name').value;
//   var last_name = document.getElementById('last_name').value;
//   var email = document.getElementById('email').value;
 
//   var mobile = document.getElementById('mobile').value;
  
   
  
 
//   if (first_name == "") {
//       showMessage('first_nameMessage1', 'First Name is required');
//       return false;
//   }
//   if (last_name == "") {
//     showMessage('last_nameMessage1', 'Last Name is required');
//     return false;
// }

   
 
// var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if(email==""){
//       showMessage('emailMessage1','Email is requred');
//       return false;
//   }
  // else if(!email.match(validRegex)){
  //     showMessage('emailMessage1','Please enter a valid email');
  //     return false;
  // }
  
   
  // if(mobile==""){
  //     showMessage('mobileMessage1','Mobile number is requred');
  //     return false;
  // }
  // else if(mobile.length !==10){
  //     showMessage('mobileMessage1','Mobile number must be 10 digit');
  //     return false;
  // }

  
// }



// function submitupdatecompany() {
//   console.log('function is called')
//   var company_name = document.getElementById('company_name').value;
//   var email = document.getElementById('email').value;
//   var mobile = document.getElementById('mobile').value;
//   var gstin = document.getElementById('gstin').value;
//   var balance = document.getElementById('balance').value;
//   var country = document.getElementById('country').value;
//   var address = document.getElementById('address').value;
  
   
  
 
//   if (company_name == "") {
//       showMessage('company_nameMessage', 'Company Name is required');
//       return false;
//   } 
// var validRegexGstin=/^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$/;
// var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if(email==""){
//       showMessage('emailMessage','Email is requred');
//       return false;
//   }
  // else if(!email.match(validRegex)){
  //     showMessage('emailMessage','Please enter a valid email');
  //     return false;
  // }
  
   
  // if(mobile==""){
  //     showMessage('mobileMessage','Mobile number is requred');
  //     return false;
  // }
  // // else if(mobile.length !==10){
  //     showMessage('mobileMessage','Mobile number must be 10 digit');
  //     return false;
  // }


  // if (gstin == "") {
  //   showMessage('gstinMessage', 'GSTIN is required');
  //   return false;
  // }

//   else if(!gstin.match(validRegexGstin)){
//     showMessage('gstinMessage','Please enter a valid GSTIN');
//      return false;
  
// }

// if(balance==""){
//   showMessage('balanceMessage','Please enter the Balance')
//   return false;
// }
//   if(country=='Select Country'){
//     showMessage('countryMessage','Please select the country')
//     return false;
//   }



//   if (address==""){
//     showMessage('addressMessage','Please enter the address ')
//     return false;
//   }
// }




// function submitaddcompany() {
//   console.log('function is called')
//   var company_name = document.getElementById('company_name1').value;
//   var email = document.getElementById('email1').value;
//   var mobile = document.getElementById('mobile1').value;
//   var gstin = document.getElementById('gstin1').value;
//   var balance = document.getElementById('balance1').value;
//   var country = document.getElementById('country1').value;
//   var address = document.getElementById('address1').value;
  
   
  
 
//   if (company_name == "") {
//       showMessage('company_nameMessage1', 'Company Name is required');
//       return false;
//   } 
// var validRegexGstin=/^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$/;
// var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
//   if(email==""){
//       showMessage('emailMessage1','Email is requred');
//       return false;
//   }
//   else if(!email.match(validRegex)){
//       showMessage('emailMessage1','Please enter a valid email');
//       return false;
//   }
  
   
//   if(mobile==""){
//       showMessage('mobileMessage1','Mobile number is requred');
//       return false;
//   }
//   else if(mobile.length !==10){
//       showMessage('mobileMessage1','Mobile number must be 10 digit');
//       return false;
//   }


//   if (gstin == "") {
//     showMessage('gstinMessage1', 'GSTIN is required');
//     return false;
//   }

//   else if(!gstin.match(validRegexGstin)){
//     showMessage('gstinMessage1','Please enter a valid GSTIN');
//      return false;
  
// }

// if(balance==""){
//   showMessage('balanceMessage1','Please enter the Balance')
//   return false;
// }
//   if(country=='Select Country'){
//     showMessage('countryMessage1','Please select the country')
//     return false;
//   }



//   if (address==""){
//     showMessage('addressMessage1','Please enter the address ')
//     return false;
//   }
// }


function submitinflowform(){
  var investor=document.getElementById('investor').value;
  var company=document.getElementById('company').value;
  var date=document.getElementById('datepicker-from').value;
  var amount=document.getElementById('amount').value;
  var description=document.getElementById('description').value;


  if(investor=="Select Investor"){
    showMessage('investorMessage','Please select investor')
    return false;
  }

  if (company=="Select Company"){
    showMessage('companyMessage','Please select the company')
    return false;
  }

   
  
  if(date==""){
    showMessage('dateMessage','Please enter date')
    return false;
  }

  if(amount==""){
    showMessage('amountMessage','Please enter amount')
    return false;
  }
 if(amount<=0){
    showMessage('amountMessage','Amount must be greater than zero')
    return false;
  }
  if (description==""){
    showMessage('descriptionMessage','Please enter the reason')
    return false;
  }
}



function submitoutflowform(){
  
  var company=document.getElementById('company1').value;
  var company2=document.getElementById('company2').value;
  var date = document.getElementById('datepicker-to').value;
  var amount=document.getElementById('amount1').value;
  var description=document.getElementById('description1').value;


  

  if (company=="Select Company"){
    showMessage('companyMessage1','Please select the company')
    return false;
  }
  if (company2=="Select Company"){
    showMessage('companyMessage2','Please select the company')
    return false;
  }
   
  
  if(date==""){
    showMessage('dateMessage1','Please enter date')
    return false;
  }
  if(amount==""){
    showMessage('amountMessage1','Please enter amount')
    return false;
  }
 if(amount<=0){
    showMessage('amountMessage1','Amount must be greater than zero')
    return false;
  }
  if (description==""){
    showMessage('descriptionMessage1','Please enter the reason')
    return false;
  }
}


    // $('#burger-button').click(function() {
        
    //     $('.navbar-nav .nav-link span').toggle();
    //     $('.side-menu .my-logo span').toggle();
    //     if ($('#sidebar').css('width') === '200px') {
    //         $('#sidebar').css('width', '');
            
    //         $('.startnav').css('margin-left', '');
    //         $('.content-wrapper').css('padding-left', '');

            
             
    //     } else {
            
    //         $('#sidebar').css('width', '200px');
    //         $('.startnav').css('margin-left', '200px');
    //         $('.content-wrapper').css('padding-left', '140px');
            
            
             
    //     }
    // });
 
   
 
      
   

 
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
  });
    
    
  
  $(document).ready(function(){
      $('.tables ').DataTable();
     
     
  });

  $(document).ready(function(){
    $("#datepicker-from, #datepicker-to").datepicker({
        dateFormat: 'dd-mm-yy'
    });
});


  $(document).on('submit','#addUserForm',function(e) {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var role = document.getElementById('role').value;
    var mobile = document.getElementById('mobile').value;
    var password=document.getElementById('password').value;
     
    
   
    if (name == "") {
        showMessage('nameMessage', 'Name is required');
        return false;
    }
  
    var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
    if(email==""){
        showMessage('emailMessage','Email is requred');
        return false;
    }
    else if(!email.match(validRegex)){
        showMessage('emailMessage','Please enter a valid email');
        return false;
    }
    console.log('lllllllllll',!email.match(validRegex))
    if(role=="Select Role"){
      showMessage('roleMessage','Please select role');
      return false;
  }
     
    if(mobile==""){
        showMessage('mobileMessage','Mobile number is requred');
        return false;
    }
    if(mobile.length !==10){
        showMessage('mobileMessage','Mobile number must be 10 digit');
        return false;
    }
  
    
    if (password==""){
      showMessage('passwordMessage','Please Enter Password')
      return false;
     } 
   
    var formData = {
        name: $('#name').val(),
        email:$('#email').val(),
        role:$('#role').val(),
        mobile:$('#mobile').val(),
        password:$('#password').val(),

    };
    $.ajax({
      url:'http://127.0.0.1:8000/add_user',
      method: 'POST',
      data:formData,
      success: function(data) {
        console.log(data)
        console.log('n values',data.n)
        if(data.n==0){
          $('#msg').html(data.msg)
          setTimeout(function() {
            document.getElementById("msg").innerText = "";
        }, 3000); 
        }
        else{
          // $('h5').html(data.msg)
          $('#add_user').modal('hide');
          $('#successMessage').text(data.msg);
          $('#successModal').modal('show');
          setTimeout(function() {
            location.reload();
        },2000);
        }
        
  
       
      }

      
    })
  });
 


var userId; 
    
function setUserId(id) {
    userId = id;  
    console.log('userId',  userId)
}


$(document).ready(function() {
  $(document).on('click', '.edit-button', function(event) {

      event.preventDefault();
      $.ajax({  
          url: 'http://127.0.0.1:8000/get_user',  
          method: 'POST',
          data: { id: userId },
          success: function(data) {
            console.log(data)
              $('#name1').val(data.name);  
              $('#email1').val(data.email);
              $('#role1').val(data.role);
              $('#mobile1').val(data.mobile);
         
         
            },
           
      });
  });

});




function submituserupdate1(e) {


  var name = document.getElementById('name1').value;
  var email = document.getElementById('email1').value;
  var role = document.getElementById('role1').value;
  var mobile = document.getElementById('mobile1').value;
   
   
  
  var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  if (name == "") {
      showMessage('nameMessage1', 'Name is required');
      
      return false;
      
  }

  if(email==""){
      showMessage('emailMessage1','Email is requred');
      
      return false;
  }
  else if(!email.match(validRegex)){
      showMessage('emailMessage1','Please enter a valid email');
      
      return false;
  }
  console.log('lllllllllll',!email.match(validRegex))
  if(role=="Select Role"){
    showMessage('roleMessage1','Please select role');
    return false;
}
   
  if(mobile==""){
      showMessage('mobileMessage1','Mobile number is requred');
      
      return false;
  }
  else if(mobile.length !==10){
      showMessage('mobileMessage1','Mobile number must be 10 digit');
       
      return false;
  }

   
  
  e.preventDefault();
  var formData = {
    id: userId,  
    name: $('#name1').val(),
    email: $('#email1').val(),
    role: $('#role1').val(),
    mobile: $('#mobile1').val(),
  }; 
 
  $.ajax({
    url:'http://127.0.0.1:8000/update_user',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg1').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg1").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#update_user').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
};

$('#update_user').submit(submituserupdate1);


$('#delete_user .yes-button').click(function(){

  $.ajax({
    url:'http://127.0.0.1:8000/delete_user',
    method: 'POST',
    data:{id:userId},
    success: function(data) {
      $('#delete_user').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');

      setTimeout(function() {
        location.reload();
    },2000);
    }

  })
});


$(document).on('submit','#addRoleForm',function(e) {
  e.preventDefault();

  var name = document.getElementById('name').value;
  name.trim();
  if (name == "") {
    showMessage('nameMessage', 'Role name  is required');
    return false;
  }
  var formData = {
      name: $('#name').val(),
      description:$('#description').val(),

  };

  console.log(formData)
  $.ajax({
    url:'http://127.0.0.1:8000/add_role',
    method: 'POST',
    data:formData,
    success: function(data) {
      
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#add_role').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
});

var roleId; 
    
function setRoleId(id) {
    roleId = id;  
    console.log('roleId',  roleId)
}


// $('.edit-role').click(function
  $(document).on('click', '.edit-role', function() {
  
  
  $.ajax({
    url:'http://127.0.0.1:8000/get_role',
    method: 'POST',
    data:{id:roleId},
    
    success: function(data) {
      console.log(data)
        $('#update_role #name1').val(data.name);
        $('#update_role #description1').val(data.description);
    }

    
  })
});



function update_role(e) {

  var name = document.getElementById('name1').value;
  name.trim();
   
  if (name == "") {
    showMessage('nameMessage1', 'Role name  is required');
    return false;
  }
  e.preventDefault();
  
  var formData = {
    id: roleId,  
    name: $('#name1').val(),
    description: $('#description1').val(),
     
  }; 
  console.log(formData)
 
  $.ajax({
    url:'http://127.0.0.1:8000/update_role',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg1').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg1").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#update_role').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
};
$('#update_role').submit(update_role);


$('#delete_role .yes-button').click(function(){

  $.ajax({
    url:'http://127.0.0.1:8000/delete_role',
    method: 'POST',
    data:{id:roleId},
    success: function(data) {
      console.log(data)
      $('#delete_role').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');

      setTimeout(function() {
        location.reload();
    },2000);
    }

  })
});




var investorId; 
    
function setInvestorId(id) {
    investorId = id;  
    console.log('investorId',  investorId)
}


$(document).on('submit','#addInvestorForm',function(e) {

  console.log('function is called')
  var first_name = document.getElementById('first_name1').value;
  var last_name = document.getElementById('last_name1').value;
  var email = document.getElementById('email1').value;
 
  var mobile = document.getElementById('mobile1').value;
  
   
  
 
  if (first_name == "") {
      showMessage('first_nameMessage', 'First Name is required');
      return false;
  }
  if (last_name == "") {
    showMessage('last_nameMessage', 'Last Name is required');
    return false;
}

   
 
var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  if(email==""){
      showMessage('emailMessage','Email is requred');
      return false;
  }
  else if(!email.match(validRegex)){
      showMessage('emailMessage','Please enter a valid email');
      return false;
  }
  
   
  if(mobile==""){
      showMessage('mobileMessage','Mobile number is requred');
      return false;
  }
  else if(mobile.length !==10){
      showMessage('mobileMessage','Mobile number must be 10 digit');
      return false;
  }

  e.preventDefault();
  var formData = {
      first_name: $('#first_name1').val(),
      last_name: $('#last_name1').val(),
      email:$('#email1').val(),
      mobile:$('#mobile1').val(),

  };

  console.log(formData)
  $.ajax({
    url:'http://127.0.0.1:8000/add_investor',
    method: 'POST',
    data:formData,
    success: function(data) {
      
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#add_investor').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
});



// $('.edit-investor').click(
  $(document).on('click', '.edit-investor', function() {
  
  console.log(investorId)
  $.ajax({
    url:'http://127.0.0.1:8000/get_investor',
    method: 'POST',
    data:{id:investorId},
    
    success: function(data) {
      console.log(data)
        $('#first_name').val(data.first_name);
        $('#last_name').val(data.last_name);
        $('#email').val(data.email);
        $('#mobile').val(data.mobile);
    }

    
  });
});






function update_investor(e) {

  console.log('function is called')
  var first_name = document.getElementById('first_name').value;
  var last_name = document.getElementById('last_name').value;
  var email = document.getElementById('email').value;
 
  var mobile = document.getElementById('mobile').value;
  
   
  
 
  if (first_name == "") {
      showMessage('first_nameMessage1', 'First Name is required');
      return false;
  }
  if (last_name == "") {
    showMessage('last_nameMessage1', 'Last Name is required');
    return false;
}

   
 
var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  if(email==""){
      showMessage('emailMessage1','Email is requred');
      return false;
  }
  else if(!email.match(validRegex)){
      showMessage('emailMessage1','Please enter a valid email');
      return false;
  }
  
   
  if(mobile==""){
      showMessage('mobileMessage1','Mobile number is requred');
      return false;
  }
  else if(mobile.length !==10){
      showMessage('mobileMessage1','Mobile number must be 10 digit');
      return false;
  }

  e.preventDefault();
  var formData = {
    id: investorId,  
    first_name: $('#first_name').val(),
    last_name: $('#last_name').val(),
    email: $('#email').val(),
    mobile: $('#mobile').val(),
     
  }; 
  console.log(formData)
 
  $.ajax({
    url:'http://127.0.0.1:8000/update_investor',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg1').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg1").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#update_investor').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
};
$('#update_investor').submit(update_investor);


$('#delete_investor .yes-button').click(function(){

  $.ajax({
    url:'http://127.0.0.1:8000/delete_investor',
    method: 'POST',
    data:{id:investorId},
    success: function(data) {
      console.log(data)
      $('#delete_investor').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');

      setTimeout(function() {
        location.reload();
    },2000);
    }

  })
});



var companyId; 
    
function setCompanyId(id) {
  companyId = id;  
    console.log('companyId',  companyId)
}


$(document).on('submit','#addCompanyForm',function(e) {
  console.log('function is called')
  var company_name = document.getElementById('company_name1').value;
  var email = document.getElementById('email1').value;
  var mobile = document.getElementById('mobile1').value;
  var gstin = document.getElementById('gstin1').value;
  var balance = document.getElementById('balance1').value;
  var country = document.getElementById('country1').value;
  var address = document.getElementById('address1').value;
  
   
  
 
  if (company_name == "") {
      showMessage('company_nameMessage1', 'Company Name is required');
      return false;
  } 
var validRegexGstin=/^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$/;
var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  if(email==""){
      showMessage('emailMessage1','Email is requred');
      return false;
  }
  else if(!email.match(validRegex)){
      showMessage('emailMessage1','Please enter a valid email');
      return false;
  }
  
   
  if(mobile==""){
      showMessage('mobileMessage1','Mobile number is requred');
      return false;
  }
  else if(mobile.length !==10){
      showMessage('mobileMessage1','Mobile number must be 10 digit');
      return false;
  }


  if (gstin == "") {
    showMessage('gstinMessage1', 'GSTIN is required');
    return false;
  }

  else if(!gstin.match(validRegexGstin)){
    showMessage('gstinMessage1','Please enter a valid GSTIN');
     return false;
  
}

if(balance==""){
  showMessage('balanceMessage1','Please enter the Balance')
  return false;
}
  if(country=='Select Country'){
    showMessage('countryMessage1','Please select the country')
    return false;
  }



  if (address==""){
    showMessage('addressMessage1','Please enter the address ')
    return false;
  }
  e.preventDefault();
  var formData = {
      company_name: $('#company_name1').val(),
      email:$('#email1').val(),
      mobile:$('#mobile1').val(),
      gstin:$('#gstin1').val(),
      balance:$('#balance1').val(),
      country:$('#country1').val(),
      address:$('#address1').val(),

  };

  
  $.ajax({
    url:'http://127.0.0.1:8000/add_company',
    method: 'POST',
    data:formData,
    success: function(data) {
     console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#add_company').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
    }

    
  })
});



// $('.edit-company').click(
  $(document).on('click', '.edit-company', function() {
  
  console.log(companyId)
  $.ajax({
    url:'http://127.0.0.1:8000/get_company',
    method: 'POST',
    data:{id:companyId},
    
    success: function(data) {
      console.log(data)
       $('#company_name').val(data.company_name);
        $('#email').val(data.email);
        $('#mobile').val(data.mobile);
        $('#gstin').val(data.gstin);
       $('#balance').val(data.balance);
       $('#country').val(data.country);
       $('#address').val(data.address);
    },
  

    
  });
});



function update_company(e) {
 
  console.log('function is called')
  var company_name = document.getElementById('company_name').value;
  var email = document.getElementById('email').value;
  var mobile = document.getElementById('mobile').value;
  var gstin = document.getElementById('gstin').value;
  var balance = document.getElementById('balance').value;
  var country = document.getElementById('country').value;
  var address = document.getElementById('address').value;
  
   
  
 
  if (company_name == "") {
      showMessage('company_nameMessage', 'Company Name is required');
      return false;
  } 
var validRegexGstin=/^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}\d{1}$/;
var validRegex =  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/ ;
  if(email==""){
      showMessage('emailMessage','Email is requred');
      return false;
  }
  else if(!email.match(validRegex)){
      showMessage('emailMessage','Please enter a valid email');
      return false;
  }
  
   
  if(mobile==""){
      showMessage('mobileMessage','Mobile number is requred');
      return false;
  }
  else if(mobile.length !==10){
      showMessage('mobileMessage','Mobile number must be 10 digit');
      return false;
  }


  if (gstin == "") {
    showMessage('gstinMessage', 'GSTIN is required');
    return false;
  }

  else if(!gstin.match(validRegexGstin)){
    showMessage('gstinMessage','Please enter a valid GSTIN');
     return false;
  
}

if(balance==""){
  showMessage('balanceMessage','Please enter the Balance')
  return false;
}
  if(country=='Select Country'){
    showMessage('countryMessage','Please select the country')
    return false;
  }



  if (address==""){
    showMessage('addressMessage','Please enter the address ')
    return false;
  }
  e.preventDefault();
  var formData = {
    id:companyId,  
    company_name: $('#company_name').val(),
      email:$('#email').val(),
      mobile:$('#mobile').val(),
      gstin:$('#gstin').val(),
      balance:$('#balance').val(),
      country:$('#country').val(),
      address:$('#address').val(),
     
  }; 
  console.log(formData)
 
  $.ajax({
    url:'http://127.0.0.1:8000/update_company',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg1').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg1").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#update_company').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
};

$('#update_company').submit(update_company);



$('#delete_company .yes-button').click(function(){

  $.ajax({
    url:'http://127.0.0.1:8000/delete_company',
    method: 'POST',
    data:{id:companyId},
    success: function(data) {
      console.log(data)
      $('#delete_company').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');

      setTimeout(function() {
        location.reload();
    },2000);
    }

  })
});




// $('#add-cashin').click(
  $(document).on('submit','#cash_in_flow',function(e) {
  e.preventDefault();
  var formData = {
      investor: $('#investor').val(),
      to_company:$('#company').val(),
      date:$('.date').val(),
      amount:$('#amount').val(),
      description:$('#description').val(),
       

  };

  
  $.ajax({
    url:'http://127.0.0.1:8000/cash_inflow',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#cash_in_flow').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
      
    }

    
  })
});




// $('#add-cashout').click(function
$(document).on('submit','#cash_out_flow',function (e) {
  e.preventDefault();
  var formData = {
      company: $('#company1').val(),
      to_company:$('#company2').val(),
      date:$('.date1').val(),
      amount:$('#amount1').val(),
      description:$('#description1').val(),
       

  };

  
  $.ajax({
    url:'http://127.0.0.1:8000/cash_outflow',
    method: 'POST',
    data:formData,
    success: function(data) {
      console.log(data)
      console.log('n values',data.n)
      if(data.n==0){
        $('#msg').html(data.msg)
        setTimeout(function() {
          document.getElementById("msg").innerText = "";
      }, 3000); 
      }
      else{
        // $('h5').html(data.msg)
        $('#cash_out_flow').modal('hide');
        $('#successMessage').text(data.msg);
        $('#successModal').modal('show');
        setTimeout(function() {
          location.reload();
      },2000);
      }
      

     
    }

    
  })
});




var inflowId; 
    
function setInflowId(id) {
  inflowId = id;  
    console.log('inflowId',inflowId)
}

$('#approve .yes-button').click(function(e) {
  e.preventDefault();  
  $.ajax({
    url:'http://127.0.0.1:8000/approved_inflow_transaction',
    method: 'POST',
    data:{id:inflowId},
    success: function(data) {
      console.log(data)
      
      $('#approve').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');
      setTimeout(function() {
        location.reload();
    },2000);

    }

    
  })
});


$('#reject .yes-button').click(function(e){
 e.preventDefault()
 $.ajax({
  url:'http://127.0.0.1:8000/rejected_inflow_transaction',
  method:'POST',
  data:{id:inflowId},
  success:function(data){
    console.log(data)
    $('#reject').modal('hide');
    $('#successMessage').text(data.msg);
    $('#successModal').modal('show');
    setTimeout(function() {
      location.reload();
  },2000);
     
  }
 })
})

var outflowId;  
function setOutflowId(id) {
  outflowId = id;  
    console.log('outflowId',outflowId)
}



$('#approve-outflow .yes-button').click(function(e) {
  e.preventDefault();  
  $.ajax({
    url:'http://127.0.0.1:8000/approved_outflow_transaction',
    method: 'POST',
    data:{id:outflowId},
    success: function(data) {
      console.log(data)
      
      $('#approve-outflow').modal('hide');
      $('#successMessage').text(data.msg);
      $('#successModal').modal('show');

      setTimeout(function() {
        location.reload();
    },2000);
    }

    
  })
});


$('#reject-outflow .yes-button').click(function(e){
 e.preventDefault()
 $.ajax({
  url:'http://127.0.0.1:8000/rejected_outflow_transaction',
  method:'POST',
  data:{id:outflowId},
  success:function(data){
    console.log(data)
    $('#reject-outflow').modal('hide');
    $('#successMessage').text(data.msg);
    $('#successModal').modal('show');
    setTimeout(function() {
      location.reload();
  },2000);
  }
 })
})

 

function handleCheckbox1(childId, parentId) {
  console.log("length",$('input.'+parentId+':checked').length)

  var checklength = $('input.'+parentId+':checked').length

  if (checklength > 0){
    $('#check'+parentId).prop('checked',true)
  }else{
    $('#check'+parentId).prop('checked',false)
  }

}

function handleCheckbox2(parentId) {
  console.log("check",$('#check'+parentId).prop('checked'))
if ($('#check'+parentId).prop('checked') == true){
  $('.'+parentId).prop('checked',true)
}else{
  $('.'+parentId).prop('checked',false)
}

}

function showMessage(elementId, message) {
document.getElementById(elementId).innerText = message;
setTimeout(function () {
    document.getElementById(elementId).innerText = "";
}, 3000); 
}

function submitFunction1(){
var role = document.getElementById('role').value;
var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
if (role == "Select Role") {
    showMessage('roleMessage', 'Please select role');
    return false;
}
else if (checkboxes.length == 0) {
    showMessage('checkMessage', 'Please select at least one permission');
    return false;
}

}



$(document).ready(function() {


$('#role').change(function() {
    var roleId = $(this).val();
    $('.mainclass').attr('checked',false)
   
        $.ajax({
            url:'http://127.0.0.1:8000/get_permissions', 
            method:'POST',
            data: {
                role: roleId
            },
            dataType: 'json',
            success: function(response) {
                 
                    console.log("response",response);

                   
                    $(response.permissions.menu).each(function (a,b){
                        console.log("b",b)
                    $('#check' + b).attr('checked', true);
                
               
               });
                
            },
             
        });
   
});
});

 
 
  // var selectedCompanyId;
  // $('#company_select').change(function() {
  //   selectedCompanyId = $(this).val(); 
  //   console.log(selectedCompanyId)
  //     });

//   $('.go-button').click(function() {
//       var companyId = $('#company_select').val();
//       var fromDate = $('#datepicker-from').val();
//       var toDate = $('#datepicker-to').val();

      
//        if(fromDate==""){
//          showMessage('dateMessage','Please enter date')
//          return false;
//        }  

//        if(toDate==""){
//          showMessage('dateMessage1','Please enter date')
//          return false;
//        }  
      
//       if(companyId==""){
//         showMessage('companyMessage','Please select company')
//         return false;
//       }  

//       if(companyId == "All") {
         
//         $.ajax({
//             type: 'POST',
//             url: 'http://127.0.0.1:8000/fetch_all_data',  
//             data: {
//                 'from_date': fromDate,
//                 'to_date': toDate
//             },
//             success: function(response) {
            
//              console.log('rrrrr',response)
//              if (response.msg) {
//               $('p').html(response.msg)
//               setTimeout(function () {
//                 document.getElementById('message').innerText = "";
//             }, 4000);
//           }

               

              
//               $(".allaccordians").html('')
              
//               $.each(response.company,function(i,val) {
//                 if (val.totalinflow==undefined){
//                   val.totalinflow=0
//                 }
//                 if (val.totaloutflow==undefined){
//                   val.totaloutflow=0
//                 }

//                 $(".allaccordians").append('<div class="container accordion" onclick="return toggleAccordion(this)"><div class="row"><div class="col-5"><span class="plus-minus "><span class="icon plus"></span></span><div  style="margin-left:20px;margin-bottom:0px;"> Company:'+  val.company_name +'<span class="company-name"></span></div></div><div class="col-4"><div>Total Inflow:'+val.totalinflow+' <span id="total-inflow"></span></div></div><div class="col-3"><div>Total Outflow:'+val.totaloutflow+' <span id="total-outflow"></span></div></div></div>'
                 

//                 ); 
                
//                 var inflow=val['inflowtransaction']
//                 console.log('companyinflow',inflow);
                
               
                
//                 $.each(inflow,function(i,val1) {
//                   $(".allaccordians").append('<h5 style="font-weight:bold;">Inflow:</h5><table  id="inflow-data"><thead style="background-color:#c1aad3;"><tr><th>Investor</th><th> To Company</th><th>Description</th><th>Date<th>Amount</th></tr></thead><tbody><tr><td>'+val1.investor+'</td><td>'+val1.to_company+'</td><td>'+val1.description+'</td><td>'+val1.date+'</td><td>'+val1.amount+'</td></tr></tbody></table>');

                   
                  
//                 });
              
//                 var outflow=val['outflowtransaction']
//                 console.log('companyoutflow',outflow);
                
//                 $.each(outflow,function(i,val2) {
//                   $(".allaccordians").append('<h5 style="font-weight:bold;">Outflow:</h5><table id="outflow-data"><thead style="background-color:#c1aad3;"><tr><th>From Company</th><th>To Company</th><th>Description</th><th>Date</th><th>Amount</th></tr></thead><tbody><tr><td>'+val2.company+'</td><td>'+val2.to_company+'</td><td>'+val2.description+'</td><td>'+val2.date+'</td><td>'+val2.amount+'</td></tr></tbody></table></div>')
                  
                  
//                 });
//                 $('.accordion').show();
//               });
           
  
//             }
          
        
//         });
//     } else {
      
//  $.ajax({
//           type: 'POST',
//           url: 'http://127.0.0.1:8000/fetch_cash_flow_data',
//           data: {
//               'company_id': companyId,
//               'from_date': fromDate,
//               'to_date': toDate
//           },
//           success: function(response) {
//               console.log(response)

//               if (response.msg) {
//                 $('p').html(response.msg)
//                 setTimeout(function () {
//                   document.getElementById('message').innerText = "";
//               }, 4000);
                
//             }
//               $('.company-name').text(response.company.company_name);
              
              
             
//               var inflowHtml = '';
//               $.each(response.inflow_in_range, function(i,inflow) {
//                   inflowHtml += '<tr><td>' + inflow.investor + '</td> <td>' + inflow.to_company + '</td><td>' + inflow.description + '</td><td>' + inflow.date + '</td><td>' + inflow.amount + '</td></tr>';
//               });
//               $('#inflow-data tbody').html(inflowHtml);
              
               
//               var outflowHtml = '';
//               $.each(response.outflow_in_range, function(i,outflow) {
//                   outflowHtml += '<tr><td>' + outflow.company + '</td><td>' + outflow.to_company + '</td><td>' + outflow.description + '</td><td>' + outflow.date + '</td><td>' + outflow.amount + '</td></tr>';
//               });
//               $('#outflow-data tbody').html(outflowHtml);

//               var totalInflowAmount = 0;
//                 $.each(response.inflow_in_range, function(i,inflow) {
//                     totalInflowAmount += inflow.amount;
//                 });
//                 $('#total-inflow').text(totalInflowAmount);

//                 var totalOutflowAmount = 0;
//                 $.each(response.outflow_in_range, function(i,outflow) {
//                     totalOutflowAmount += outflow.amount;
//                 });
//                 $('#total-outflow').text(totalOutflowAmount);

//                 $('.accordion').show();

                
//           }
        
//       });
//     }
//   });


var selectedCompanyId;
$('#company_select').change(function() {
  selectedCompanyId = $(this).val(); 
  console.log(selectedCompanyId)
    });

    
$('.go-button').click(function() {
  var companyId = $('#company_select').val();
  var fromDate = $('#datepicker-from').val();
  var toDate = $('#datepicker-to').val();

  
   if(fromDate==""){
     showMessage('dateMessage','Please enter date')
     return false;
   }  

   if(toDate==""){
     showMessage('dateMessage1','Please enter date')
     return false;
   }  
  
  if(companyId==""){
    showMessage('companyMessage','Please select company')
    return false;
  }  

  if(companyId == "All") {
     
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/fetch_all_data',  
        data: {
            'from_date': fromDate,
            'to_date': toDate
        },
        success: function(response) {
        
         console.log('rrrrr',response)
         if (response.msg) {
          $('p').html(response.msg)
          setTimeout(function () {
            document.getElementById('message').innerText = "";
        }, 4000);
      }

          
          var accordiondata ='';
          $.each(response.company,function(i,val) {
           
            var totalinflow =val['totalinflow']
            console.log('total',totalinflow)
            console.log('company response',response.company)
            console.log('company response',val.company_name)
            if (val.totalinflow==undefined){
              val.totalinflow=0
            }
            if (val.totaloutflow==undefined){
              val.totaloutflow=0
            }
            
            accordiondata +=' <div class="accordion-item" style="margin-bottom:5px;"><div style="background-color:#9075a4;color: white;"><h2 class="accordion-header" id="flush-headingOne"><div class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne_'+val.id+'"  aria-controls="flush-collapseOne_'+val.id+'" aria-expanded="true" style="padding:0px;"><div style="display:flex; justify-content:space-between;background-color:#9075a4;color:white; height:50px; padding-top:13px; font-weight:bold; padding-left:10px; cursor:pointer;"><div class="col-4">Company:'+val.company_name+'</div><div class="col-4">Total Inflow:'+val.totalinflow+'</div><div class="col-4">Total Outflow:'+val.totaloutflow+'</div></div></div></h2></div><div id="flush-collapseOne_'+val.id+'" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample"><div class="accordion-body"><h5 style="font-weight:bold">Inflow:</h5><table id="inflow-data"><thead style="background-color: #c1aad3"><tr><th>Investor</th><th>To Company</th><th>Description</th><th>Date</th><th>Amount</th></tr></thead><tbody><tr><td>'+val.inflowtransaction.map(s => s.investor).join('<br/>')+'</td><td>'+val.inflowtransaction.map(s => s.to_company).join('<br/>')+'</td><td>'+val.inflowtransaction.map(s => s.description).join('<br/>')+'</td><td>'+val.inflowtransaction.map(s => s.date).join('<br/>')+'</td><td>'+val.inflowtransaction.map(s => s.amount).join('<br/>')+'</td></tr></tbody></table><h5 style="font-weight: bold">Outflow:</h5><table id="outflow-data"><thead style="background-color: #c1aad3"><tr><th>From Company</th><th>To Company</th><th>Description</th><th>Date</th><th>Amount</th></tr></thead><tbody><tr><td>'+val.outflowtransaction.map(p => p.company).join('<br/>')+'</td><td>'+val.outflowtransaction.map(p => p.to_company).join('<br/>')+'</td><td>'+val.outflowtransaction.map(p => p.description).join('<br/>')+'</td><td>'+val.outflowtransaction.map(p => p.date).join('<br/>')+'</td><td>'+val.outflowtransaction.map(p => p.amount).join('<br/>')+'</td></tr></tbody></table></div></div></div>';
            
              
          });
         
          $('#accordionFlushExample').html(accordiondata)
       

        }
      
    
    });
} else {
  
$.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8000/fetch_cash_flow_data',
      data: {
          'company_id': companyId,
          'from_date': fromDate,
          'to_date': toDate
      },
      success: function(response) {
          console.log(response)

          if (response.msg) {
            $('p').html(response.msg)
            setTimeout(function () {
              document.getElementById('message').innerText = "";
          }, 4000);
            
        }
         

            
          var accordiondata ='';
          $.each(response.company,function(i,val) {
             
             
           
            console.log("val",val)
            if (val.totalinflow==undefined){
              val.totalinflow=0
            }
            if (val.totaloutflow==undefined){
              val.totaloutflow=0
            }

            accordiondata +=' <div class="accordion-item" style="margin-bottom:5px;"><div style="background-color:#9075a4;color: white;"><h2 class="accordion-header" id="flush-headingOne"><div class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne_'+val.id+'"  aria-controls="flush-collapseOne_'+val.id+'" aria-expanded="true" style="padding:0px;"><div style="display:flex; justify-content:space-between;background-color:#9075a4;color:white; height:50px; padding-top:13px; font-weight:bold; padding-left:10px; cursor:pointer;"><div class="col-4">Company:'+val.company_name+'</div><div class="col-4">Total Inflow:'+val.totalinflow+'</div><div class="col-4">Total Outflow:'+val.totaloutflow+'</div></div></div></h2></div><div id="flush-collapseOne_'+val.id+'" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample"><div class="accordion-body"><h5 style="font-weight:bold">Inflow:</h5><table id="inflow-data"><thead style="background-color: #c1aad3"><tr><th>Investor</th><th>To Company</th><th>Description</th><th>Date</th><th>Amount</th></tr></thead><tbody><tr><td>'+response.inflow_in_range.map(s => s.investor).join('<br/>')+'</td><td>'+response.inflow_in_range.map(s => s.to_company).join('<br/>')+'</td><td>'+response.inflow_in_range.map(s => s.description).join('<br/>')+'</td><td>'+response.inflow_in_range.map(s => s.date).join('<br/>')+'</td><td>'+response.inflow_in_range.map(s => s.amount).join('<br/>')+'</td></tr></tbody></table><h5 style="font-weight: bold">Outflow:</h5><table id="outflow-data"><thead style="background-color: #c1aad3"><tr><th>From Company</th><th>To Company</th><th>Description</th><th>Date</th><th>Amount</th></tr></thead><tbody><tr><td>'+response.outflow_in_range.map(p => p.company).join('<br/>')+'</td><td>'+response.outflow_in_range.map(p => p.to_company).join('<br/>')+'</td><td>'+response.outflow_in_range.map(p => p.description).join('<br/>')+'</td><td>'+response.outflow_in_range.map(p => p.date).join('<br/>')+'</td><td>'+response.outflow_in_range.map(p => p.amount).join('<br/>')+'</td></tr></tbody></table></div></div></div>';
            
              
          });
         
          $('#accordionFlushExample').html(accordiondata)
       
      }
    
  });
}
});

  $(document).ready(function(){

    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8000/get_role_list',
    
     success: function(response) {
      
       
     
      var bodyofrole=''
      $.each(response, function(k, v) {
       
        if(v.description==null){
          v.description="No description"
        }
        
       bodyofrole+='<tr><td class="text-center">' + v.name + '</td><td class="text-center">' + v.description + '</td><td class="text-center"> <a href=" " onclick="setRoleId('+ v.id +')" data-bs-toggle="modal" data-bs-target="#update_role"   class="edit-role btn bg-success"   data-toggle="tooltip" data-placement="top" title="Edit"><i class="fa fa-edit"></i></a> <a href="" onclick="setUserId('+ v.id +')" data-bs-toggle="modal" data-bs-target="#delete_role"  class="delete-button btn  bg-danger"  data-toggle="tooltip" data-placement="top" title="Delete" ><i class="fa fa-trash"></i> </td></tr>';
      


     
    });
 $('#bodyofrole').html(bodyofrole)
  }
    });
  });


  // $(document).ready(function(){
  //   $.ajax({
      
  //     url: 'http://127.0.0.1:8000/send_email',
  //     method: 'POST',
    
  //    success: function(response) {
  //   console.log(response)
  //   if(response.n==1){
  //     console.log('sent')
  //   }
  //    }
  //   });
  // })