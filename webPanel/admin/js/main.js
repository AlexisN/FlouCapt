/**
*	FlouCapt main.js
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/

$(document).ready(function()
{
    $('#boxHelp').hide();


//validate checkbox and radio groups
function validateCheckRadio(){
    var err = {};

    $('.radio-group, .checkbox-group').each(function(){
        if($(this).hasClass('required'))
            if (!$(this).find('input:checked').length)
                err[$(this).find('input:first').attr('name')] = 'Please complete this mandatory field.';
        });

    if (!$.isEmptyObject(err)){
        validator.invalidate(err);
        return false
    }
    else return true;

}

//clear any checkbox errors
function clearCheckboxError(input){
    var parentDiv = input.parents('.field');

    if (parentDiv.hasClass('required'))
        if (parentDiv.find('input:checked').length > 0){
            validator.reset(parentDiv.find('input:first'));
            parentDiv.find('.error').remove();
        }
    }




//Position the error messages next to input labels
$.tools.validator.addEffect("labelMate", function(errors, event){
    $.each(errors, function(index, error){
        error.input.first().parents('.field').find('.error').remove().end().find('label').after('<span class="error">' + error.messages[0] + '</span>');
    });

}, function(inputs){
    inputs.each(function(){
        $(this).parents('.field').find('.error').remove();
    });

});


/**
* Handle the form submission, display success message if
* no errors are returned by the server. Call validator.invalidate
* otherwise.
*/

$(".TTWForm").validator({effect:'labelMate'}).submit(function(e){
    var form = $(this), checkRadioValidation = validateCheckRadio();

    if(!e.isDefaultPrevented() && checkRadioValidation){
        $.post(form.attr('action'), form.serialize(), function(data){
            data = $.parseJSON(data);

            if(data.status == 'success'){
                form.fadeOut('fast', function(){
                    $('#boxHelp').hide();
                    $('.confirm').hide();
                    $('.TTWForm-container').append('<h2 class="success-message">Success!<BR><a href="admin.php"> Return</a></h2>');
                });
            }
            else validator.invalidate(data.errors);

        });
    }

    return false;
});

var validator = $('.TTWForm').data('validator');


});
function divHelp(num){

    var explain = ["You can enter here (or modify) the IP of the camera which will be used for the application.", 
    "Must be a number. With this parameter, you can choose how fast pictures are take. (in seconds)", 
    "Allowed you to define the name of the website which will appear on the tab.", 
    "Enter here the link of the advertisement which appears at the bottom of the first page.", 
    "Enter here the link of the website that will be showed if the user click on the advertisement 1.", 
    "Enter here the link of the advertisement which appears at the bottom of the second page. ", 
    "Enter here the link of the website that will be showed if the user click on the advertisement 2.", 
    "Must be a number.Enter here how long the advertisement 1 has to be visible on the first page (in milliseconds).", 
    "Must be a number.How fast the advertisement 1 has to come back on the screen. (in millisecond)", 
    "You can enter here some informations that will be showed on the second page. Please use HTML tag.", 
    "Change admin Password"];

    $('#boxHelp').text(explain[num]); 
    $('#boxHelp').fadeIn(); }