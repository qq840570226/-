using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TensorFlow;

namespace JustForTest
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var s = new TFSession())
            {
                var g = s.Graph;

                //建立两个TFOutput，都是常数
                var v1 = g.Const(1.5);
                var v2 = g.Const(0.5);

                //建立一个相加的运算
                var add = g.Add(v1, v2);

                //获得runner
                var runner = s.GetRunner();

                //相加
                var result = runner.Run(add);

                //获得result的值2
                Console.WriteLine($"相加的结果:{result.GetValue()}");
            }
            Console.Read();
        }
    }
}
