import re

html_file = 'c:/laragon/www/Rainbownies/index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

updates = {
    "Netflix": '''[
                    {
                        name: "Sharing 1U",
                        options: [
                            { duration: "1 hari", price: "6k" },
                            { duration: "3 hari", price: "13k" },
                            { duration: "7 hari", price: "14k" },
                            { duration: "1 bulan", price: "38k" },
                            { duration: "2 bulan", price: "70k" }
                        ]
                    },
                    {
                        name: "Sharing 2U",
                        options: [
                            { duration: "1 bulan", price: "30k" },
                            { duration: "2 bulan", price: "40k" },
                            { duration: "3 bulan", price: "58k" }
                        ]
                    },
                    {
                        name: "Semi Private",
                        options: [
                            { duration: "1 bulan", price: "44k" },
                            { duration: "2 bulan", price: "85k" }
                        ]
                    }
                ]''',
    "Viu": '''[
                    {
                        name: "Private",
                        options: [
                            { duration: "1 hari", price: "2k" },
                            { duration: "3 hari", price: "4k" },
                            { duration: "7 hari", price: "5k" },
                            { duration: "1 bulan", price: "10k" },
                            { duration: "2 bulan", price: "15k" },
                            { duration: "3 bulan", price: "20k" },
                            { duration: "6 bulan", price: "25k" },
                            { duration: "1 tahun", price: "30k" },
                            { duration: "2 tahun", price: "35k" }
                        ]
                    }
                ]''',
    "LokLok": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 hari", price: "4k" },
                            { duration: "6 hari", price: "10k" },
                            { duration: "17 hari", price: "18k" },
                            { duration: "1 bulan", price: "25k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 hari", price: "6k" },
                            { duration: "6 hari", price: "13k" },
                            { duration: "11 hari", price: "19k" },
                            { duration: "1 bulan", price: "55k" }
                        ]
                    }
                ]''',
    "Disney+": '''[
                    {
                        name: "Sharing 3U",
                        options: [
                            { duration: "1 hari", price: "8k" },
                            { duration: "3 hari", price: "10k" },
                            { duration: "7 hari", price: "18k" },
                            { duration: "1 bulan", price: "33k" }
                        ]
                    },
                    {
                        name: "Sharing 6U",
                        options: [
                            { duration: "1 hari", price: "7k" },
                            { duration: "3 hari", price: "8k" },
                            { duration: "5 hari", price: "10k" },
                            { duration: "1 bulan", price: "30k" }
                        ]
                    }
                ]''',
    "YouTube": '''[
                    {
                        name: "FamPlan",
                        options: [
                            { duration: "1 bulan", price: "8k" },
                            { duration: "2 bulan", price: "12k" }
                        ]
                    },
                    {
                        name: "IndPlan",
                        options: [
                            { duration: "1 bulan", price: "15k" },
                            { duration: "44 hari fullgar", price: "23k" },
                            { duration: "3 bulan nogar", price: "38k" },
                            { duration: "3 bulan fullgar", price: "45k" }
                        ]
                    },
                    {
                        name: "MixPlan",
                        options: [
                            { duration: "3 bulan", price: "22k" }
                        ]
                    }
                ]''',
    "WeTV": '''[
                    {
                        name: "Sharing 6U",
                        options: [
                            { duration: "1 hari", price: "4k" },
                            { duration: "3 hari", price: "6k" },
                            { duration: "7 hari", price: "8k" },
                            { duration: "1 bulan", price: "11k" }
                        ]
                    },
                    {
                        name: "Sharing 3U",
                        options: [
                            { duration: "1 bulan", price: "17k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 bulan", price: "38k" }
                        ]
                    }
                ]''',
    "Vidio": '''[
                    {
                        name: "Sharing 2U - All Device",
                        options: [
                            { duration: "1 hari", price: "7k" },
                            { duration: "3 hari", price: "10k" },
                            { duration: "7 hari", price: "14k" },
                            { duration: "1 bulan", price: "27k" }
                        ]
                    },
                    {
                        name: "Private All Device",
                        options: [
                            { duration: "1 hari", price: "10k" },
                            { duration: "3 hari", price: "13k" },
                            { duration: "7 hari", price: "19k" },
                            { duration: "1 bulan", price: "40k" }
                        ]
                    }
                ]''',
    "Moviebox": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "8k" },
                            { duration: "3 bulan", price: "12k" },
                            { duration: "1 tahun", price: "18k" }
                        ]
                    }
                ]''',
    "Bstation Premium": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "9k" },
                            { duration: "3 bulan", price: "12k" },
                            { duration: "1 tahun", price: "18k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 bulan", price: "38k" }
                        ]
                    }
                ]''',
    "iQIYI": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 hari", price: "4k" },
                            { duration: "3 hari", price: "5k" },
                            { duration: "1 bulan", price: "14k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 bulan", price: "38k" }
                        ]
                    }
                ]''',
    "Spotify": '''[
                    {
                        name: "IndPlan",
                        options: [
                            { duration: "1 bulan", price: "28k" },
                            { duration: "3 bulan", price: "47k" }
                        ]
                    },
                    {
                        name: "FamPlan",
                        options: [
                            { duration: "1 bulan", price: "30k" }
                        ]
                    },
                    {
                        name: "Ind-Student",
                        options: [
                            { duration: "1 bulan", price: "22k" }
                        ]
                    }
                ]''',
    "Scribd": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "14k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
                            { duration: "1 bulan", price: "24k" }
                        ]
                    }
                ]''',
    "iLovePDF": '''[
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "13k" }
                        ]
                    },
                    {
                        name: "Private",
                        options: [
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
        print(f"Failed to update {name}")

# Now inject Iflix
iflix_obj = '''            {
                id: 31,
                name: "Iflix",
                category: "streaming",
                packages: [
                    {
                        name: "Sharing",
                        options: [
                            { duration: "1 bulan", price: "8k" },
                            { duration: "3 bulan", price: "10k" },
                            { duration: "1 tahun", price: "20k" }
                        ]
                    }
                ]
            }'''

if 'name: "Iflix"' not in html:
    html = html.replace('        ];', '        },\n' + iflix_obj + '\n        ];', 1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print("Update complete")
