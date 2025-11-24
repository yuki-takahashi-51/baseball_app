from pathlib import Path
import os
#ここで使用している環境変数は、start.shに格納してあります
#通信確立時にsystemctlを利用し、start.shを実行することでサーバーの起動が自動で可能です
#セキュリティの観点からstart.shは公開できません。また、公開にあたり一部変更しています

#Djangoに備わっているuser機能だが自分でuserテーブルを定義したためそれを参照するように記述
AUTH_USER_MODEL = 'player_app.User'

#BASEのままだと上から3番目の階層を探索するため自分で二番目の階層のtemplatesを探索するよう指示
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

#環境変数で安全に保管
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

#環境変数で安全に保管
ALLOWED_HOSTS = os.environ['DJANGO_ALLOWED_HOSTS'].split(',') 

#ドメイン以外からの送信は拒否
CSRF_TRUSTED_ORIGINS = [
    "https://playerdataapp.com",
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

#作成するアプリも登録しておく
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'player_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'player_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],#上で定義したものだがここに入れないと動作しない
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'player_project.wsgi.application'


#DBのセッティングを行う 環境変数で安全に保管
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
        'HOST': os.environ['DJANGO_DB_HOST'],
        'PORT': os.environ['DJANGO_DB_PORT'],
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#タイムゾーンと言語を変更
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

#CSRFトークンの入ったクッキーはHTTPSでしか送れない　中間者攻撃対策
CSRF_COOKIE_SECURE = True
#セッションIDの入ったクッキーはHTTPSでしか送れない
SESSION_COOKIE_SECURE = True
#Nginx→DjangoのHTTPをHTTPSと認識させる　Nginx.confも設定
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#HTTPS通信の強制
SECURE_SSL_REDIRECT = True
#ブラウザのXSSフィルタを有効に　スクリプト挿入を阻止
SECURE_BROWSER_XSS_FILTER = True
#Content-typeの指定を強制　勝手な推測の禁止
SECURE_CONTENT_TYPE_NOSNIFF = True
#勝手な埋め込みを禁止　クリックジャッキングの防止　
X_FRAME_OPTIONS = 'DENY'
#ブラウザに1時間間隔でHTTPS強制を通知
SECURE_HSTS_SECONDS = 3600
#上記の通知をサブドメインにも適用　今はないが拡張用
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#ブラウザが初回アクセス以前からHTTPSを強制
SECURE_HSTS_PRELOAD = True
    
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
