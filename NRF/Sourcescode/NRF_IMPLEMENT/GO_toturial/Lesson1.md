# Tìm hiểu cơ bản về GOLAMG 
## SYNTAX 

1 chương trình golang bao gồm 4 thành phần chính
 Package declaration : tên packages - tương tự với JAVA thì mỗi code đóng gói package chúng ta có thể sử dụng bằng các 
 ````
   package main

 ````
 Import packages : các gói được khai báo bên ngoài ( nguồn github,web,vvvvv)
 ````
 import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/asaskevich/govalidator"
	"github.com/urfave/cli"

	"github.com/free5gc/nrf/internal/logger"
	"github.com/free5gc/nrf/internal/util"
	nrf_service "github.com/free5gc/nrf/pkg/service"
	"github.com/free5gc/util/version"
    )
 ````
 Functions : Hàm, Chương trình được chúng ta viết và định nghĩa
 ````
 func main() {
	app := cli.NewApp()
	app.Name = "nrf"
	app.Usage = "5G Network Repository Function (NRF)"
	app.Action = action
	app.Flags = NRF.GetCliCmd()
	if err := app.Run(os.Args); err != nil {
		logger.AppLog.Errorf("NRF Run Error: %v\n", err)
	}
}
 ````
 Statements and Expressions : Báo cáo và biểu thức
 