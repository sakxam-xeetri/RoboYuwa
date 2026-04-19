// Function to parse the simple .env file dynamically on the client side
async function loadEnv() {
    try {
        const response = await fetch('.env');
        const text = await response.text();
        const env = {};
        text.split('\n').forEach(line => {
            const match = line.match(/^\s*([\w]+)\s*=\s*(.*)?\s*$/);
            if (match) {
                let key = match[1];
                let value = match[2].replace(/^["']|["']$/g, '').trim();
                env[key] = value;
            }
        });
        return env;
    } catch (error) {
        console.error("Failed to load .env configuration:", error);
        return null;
    }
}

// Initialize EmailJS mechanism
document.addEventListener("DOMContentLoaded", async () => {
    const contactForm = document.getElementById("contact-form");
    if (!contactForm) return; // Exit if not on the contact page

    // Attempt to load the .env environment variables configured by the user
    const envData = await loadEnv();
    if (envData && envData.EMAILJS_PUBLIC_KEY && emailjs) {
        // Initialize EmailJS with the public key from .env
        emailjs.init(envData.EMAILJS_PUBLIC_KEY);
    } else {
        console.warn("EmailJS initialization issue: missing env config or library.");
    }

    contactForm.addEventListener("submit", function (e) {
        e.preventDefault();

        // Ensure envData and EmailJS are properly loaded before continuing
        if (!envData || !envData.EMAILJS_SERVICE_ID || !envData.EMAILJS_TEMPLATE_ID) {
            alert("Contact service configuration missing. Please verify the .env settings.");
            return;
        }

        // Grab the native submit button to switch state
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = "Sending...";
        submitBtn.disabled = true;

        // EmailJS allows passing arbitrary parameters into your templates.
        // We explicitly pass the forwarded email dictated in the .env along with user inputs
        const templateParams = {
            forward_to_email: envData.FORWARD_TO_EMAIL,
            from_name: document.getElementById('name').value,
            from_email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        emailjs.send(envData.EMAILJS_SERVICE_ID, envData.EMAILJS_TEMPLATE_ID, templateParams)
            .then(function (response) {
                alert("Message sent successfully!");
                contactForm.reset();
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            }, function (error) {
                console.error("FAILED...", error);
                alert("Failed to send message: " + JSON.stringify(error));
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            });
    });
});
