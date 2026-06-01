# Al Jazeera 360 MCP Server 🎬

خادم بروتوكول سياق النموذج (Model Context Protocol - MCP) متكامل ومحترف لمنصة البث المرئي الرقمية **الجزيرة 360 (Al Jazeera 360)**.

يتيح هذا الخادم لوكلاء ومساعدي الذكاء الاصطناعي (مثل Claude و ChatGPT) الاتصال مباشرة بقاعدة بيانات ومحتوى منصة الجزيرة 360، والبحث عن البرامج والوثائقيات والمسلسلات، وجلب تفاصيل الفيديوهات وحلقات المواسم بشكل تلقائي وفوري مع روابط المشاهدة المباشرة على المنصة.

---

## 🚀 الميزات والأدوات المتاحة (Tools)

يحتوي الخادم على **8 أدوات ذكية ومختبرة** تعمل بكفاءة عالية:

| الأداة (Tool) | الوصف (Description) | الاستخدام (Usage) |
| :--- | :--- | :--- |
| `list_sections` | عرض جميع الأقسام والقنوات المتاحة (15 قسم) | لمعرفة معرفات الأقسام المتاحة للتصفح |
| `get_trending_content` | جلب المحتوى الرائج والأكثر مشاهدة والمميز على الصفحة الرئيسية | لعرض ترشيحات يومية للمستخدمين |
| `browse_section` | تصفح محتوى قسم محدد بالكامل (مثل: وثائقيات، بودكاست، برامج حوارية) | لاستكشاف البرامج داخل تصنيف معين |
| `get_video_details` | جلب معلومات تفصيلية عن فيديو محدد (العنوان، الوصف، المدة، الجودة حتى 4K) | لعرض بطاقة معلومات الفيديو قبل المشاهدة |
| `get_series_details` | جلب تفاصيل مسلسل أو برنامج (مثل: الدحيح) مع قائمة المواسم المتاحة | لاستكشاف بنية البرامج متعددة المواسم |
| `get_season_episodes` | جلب قائمة الحلقات الكاملة داخل موسم محدد | للوصول للحلقات الفردية وروابط تشغيلها |
| `search_videos` | بحث شامل فائق السرعة بالعربية والإنجليزية في كل محتوى المنصة | للبحث عن مواضيع محددة (مثل: "غزة"، "فلسطين") |
| `get_latest_episodes` | جلب أحدث الحلقات المضافة حديثاً لقسم معين (مثل قناة الجزيرة) | لمتابعة المستجدات والبرامج اليومية |

---

## 🛠️ المتطلبات الفنية (Prerequisites)

- **Python**: إصدار 3.10 أو أحدث.
- **المكتبات الأساسية**: `mcp`, `httpx`, `uvicorn`.

---

## 💻 التثبيت والتشغيل المحلي (Local Setup)

### 1. تثبيت الاعتمادات
```bash
pip install -r requirements.txt
```

### 2. تشغيل خادم الاختبار
لتجربة الخادم والتأكد من اتصال الـ APIs بنجاح:
```bash
python test_server.py
```

### 3. ربطه مع Claude Desktop
أضف الإعدادات التالية إلى ملف `claude_desktop_config.json` الخاص بك:

**على نظام Windows:**
`%APPDATA%\Channel\Claude\claude_desktop_config.json`

**على نظام macOS:**
`~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "aljazeera360": {
      "command": "python",
      "args": [
        "/path/to/aljazeera360-mcp-server/server.py"
      ],
      "env": {
        "AJ360_AUTH_TOKEN": "YOUR_FIREBASE_AUTH_TOKEN_HERE"
      }
    }
  }
}
```

*ملاحظة: السيرفر يعمل تلقائياً بوضع الزائر (Guest Mode) إذا لم يتم توفير الـ Token، ولكن يفضل توفيره للوصول الكامل للمحتوى.*

---

## 🌐 النشر السحابي (Cloud Deployment)

السيرفر جاهز تماماً للنشر على **Google Cloud Run** أو **Render** كحاوية Docker.

### Dockerfile المرفق:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["mcp", "run", "server.py"]
```

---

## 📊 البنية التحتية المكتشفة للـ API (Vesper/Dice Platform)

تم بناء هذا الخادم بعد تحليل معمق للطلبات الموجهة لخوادم منصة **Vesper/Dice** الشريك التقني للجزيرة 360:
- **بوابة الـ API**: `https://dce-frontoffice.imggaming.com`
- **محرك البحث**: `https://search.dce-prod.dicelaboratory.com`
- **مفتاح التطبيق**: `857a1e5d-e35e-4fdf-805b-a87b6f8364bf` (ثابت ومصرح به للمنصة)
- **المجال (Realm)**: `dce.aljazeera`
