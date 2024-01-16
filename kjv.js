document.addEventListener('DOMContentLoaded', function () {
    const bibleVersesContainer = document.querySelector('.pane p');
    const shareToWhatsAppContainer = document.getElementById('shareToWhatsApp');

    // Array of Bible verses for Revelation chapter 1
    const revelationChapter1 = [
        "Revelation 1:1 - The revelation of Jesus Christ, which God gave unto him, to shew unto his servants things which must shortly come to pass; and he sent by his angel unto his servant John:",
        "Revelation 1:2 - Who bare record of the word of God, and of the testimony of Jesus Christ, and of all things that he saw.",
        // Add more verses as needed
    ];

    // Function to get and display two Bible verses daily
    function getDailyBibleVerses() {
        const currentDate = new Date();
        const dayOfYear = Math.floor((currentDate - new Date(currentDate.getFullYear(), 0, 0)) / 86400000);
        const verseIndex = dayOfYear % revelationChapter1.length;

        // Displaying two verses
        bibleVersesContainer.textContent = revelationChapter1[verseIndex];
        const nextVerseIndex = (verseIndex + 1) % revelationChapter1.length;
        bibleVersesContainer.textContent += `\n${revelationChapter1[nextVerseIndex]}`;
    }

    // Function to generate WhatsApp share link
    function generateWhatsAppShareLink() {
        const shareText = encodeURIComponent(`Check out today's Bible verses: ${revelationChapter1.join('\n')}`);
        const whatsappLink = `https://wa.me/?text=${shareText}`;
        shareToWhatsAppContainer.innerHTML = `<a href="${whatsappLink}" target="_blank"><i class="fab fa-whatsapp"></i></a>`;
    }

    // Function to refresh Bible verses and WhatsApp share link daily
    function refreshContentDaily() {
        getDailyBibleVerses(); // Initial load
        generateWhatsAppShareLink(); // Initial load
        setInterval(() => {
            getDailyBibleVerses();
            generateWhatsAppShareLink();
        }, 24 * 60 * 60 * 1000); // Refresh every 24 hours
    }

    refreshContentDaily(); // Start the process
});
