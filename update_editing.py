import re

html_file = 'c:/laragon/www/Rainbownies/index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

updates = {
    "Capcut Pro": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 hari", price: "3k" },
                            { duration: "3 hari", price: "7k" },
                            { duration: "7 hari", price: "17k" },
                            { duration: "1 bulan", price: "20k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 hari", price: "7k" },
                            { duration: "3 hari", price: "13k" },
                            { duration: "1 bulan", price: "40k" }
                        ]
                    }
                ]''',
    "Canva": '''[
                    {
                        name: "Canva Pro",
                        options: [
                            { duration: "1 hari", price: "2k" },
                            { duration: "3 hari", price: "3k" },
                            { duration: "7 hari", price: "6k" },
                            { duration: "1 bulan", price: "10k" },
                            { duration: "2 bulan", price: "13k" },
                            { duration: "3 bulan", price: "17k" }
                        ]
                    },
                    {
                        name: "Lifetime",
                        options: [
                            { duration: "Garansi 6 bulan", price: "38k" },
                            { duration: "Garansi 1 tahun", price: "45k" }
                        ]
                    }
                ]''',
    "Alight Motion": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "5k" },
                            { duration: "1 tahun", price: "15k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 bulan", price: "10k" },
                            { duration: "1 tahun", price: "25k" }
                        ]
                    }
                ]''',
    "Duolingo Plus": '''[
                    {
                        name: "FamPlan",
                        options: [
                            { duration: "1 bulan", price: "16k" },
                            { duration: "2 bulan", price: "26k" },
                            { duration: "3 bulan", price: "36k" }
                        ]
                    }
                ]''',
    "Wink": '''[
                    {
                        name: "Private",
                        options: [
                            { duration: "7 hari", price: "16k" }
                        ]
                    }
                ]''',
    "Meitu": '''[
                    {
                        name: "Private",
                        options: [
                            { duration: "7 hari (Andro Only)", price: "14k" },
                            { duration: "21 hari (IOS/Android)", price: "34k" }
                        ]
                    }
                ]''',
    "Picsart": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "7 hari", price: "7k" },
                            { duration: "1 bulan", price: "13k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "7 hari", price: "9k" },
                            { duration: "1 bulan", price: "20k" }
                        ]
                    }
                ]'''
}

for name, new_packages in updates.items():
    pattern = r'(name:\s*"' + re.escape(name) + r'",\s*category:\s*"[^"]+",\s*packages:\s*\[).*?(\n\s{16}\])'
    def replacer(m):
        return m.group(1) + new_packages[1:]
    html, count = re.subn(pattern, replacer, html, flags=re.DOTALL)
    if count == 0:
        print(f"Failed to update packages for {name}")

# Also assure category is 'editing' for Picsart, Meitu, Wink just in case
category_updates = ["Picsart", "Meitu", "Wink"]
for name in category_updates:
    pattern_cat = r'(name:\s*"' + re.escape(name) + r'",\s*category:\s*")[^"]+(")'
    html = re.sub(pattern_cat, r'\g<1>editing\g<2>', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Update complete")
