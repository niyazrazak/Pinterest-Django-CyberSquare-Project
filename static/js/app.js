console.log("Index page");
$(document).ready(function($) {
    $("#loginformuser").validate({
        rules: {
            password: {
                required: true,
                minlength: 6,
            },
            email: {
                required: true,
                email: true,
            },
        },
        messages: {
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 6 characters long",
            },
            email: "Please enter your email",
        },
    });
    $("#signupform").validate({
        rules: {
            first_name: {
                required: true,
                minlength: 3,
            },
            last_name: {
                required: true,
                minlength: 3,
            },
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 6,
            },
            mobile: "required",
        },
        messages: {
            first_name: {
                required: "Please Enter First Name",
                minlength: "Atleast 3 Characters",
            },
            last_name: {
                required: "Please Enter Last Name",
                minlength: "Atleast 3 Characters",
            },
            password: {
                required: "Please Provide A Password",
                minlength: "Your Password Must be at least 6 characters long",
            },
            email: "Please Enter Your Email",
            mobile: "Please Enter Your Number",
        },
    });
});