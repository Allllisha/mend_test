// Mendスキャン練習用の小さなWebアプリ。
// go.mod の古いライブラリを実際に import して使うことで、
// Reachability（脆弱なコードに到達するか）の分析対象になるようにしている。
// 動かすことが目的ではなく、スキャンされることが目的。
package main

import (
	"net/http"

	jwt "github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
	"golang.org/x/text/language"
)

const secret = "practice-secret" // 練習用。実案件ではコードに書かない

func main() {
	r := gin.Default()

	r.GET("/", func(c *gin.Context) {
		tag := language.Make(c.DefaultQuery("lang", "ja"))
		c.JSON(http.StatusOK, gin.H{"lang": tag.String()})
	})

	r.GET("/token", func(c *gin.Context) {
		token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{"user": "arisa"})
		signed, err := token.SignedString([]byte(secret))
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"token": signed})
	})

	r.Run(":8080")
}
