---
title:  "A simple client-server program using Java Socket"
categories: [Distributed Systems]
tags: [Socket]
mathjax: true
---
<a name="introduction"></a>
## Definition of Socket in Java
A socket is **one endpoint** of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
<a name="prerequisites"></a>
## Prerequisites
* [Homebrew](https://docs.brew.sh/Installation.html)
<a name="java"></a>
* **Java6 or above (you can download java with following commands. Note //... are comments and should not be put into the terminal)**
{% highlight bash %}
brew tap caskroom/cask // install cask
brew cask install java // install Java
brew cask info java    // verify which java version has been installed
{% endhighlight %}

<a name="main"></a>
## A simple Client-Server program using Java Socket
Compile Client.java and Server.java (see attached codes). Note //... are comments and should not be put into the terminal:
{% highlight bash %}
javac *.java // compile files end with .java and will generate Client.class and Server.class files
java Server // start Server
java Client // open another terminal and start Client
{% endhighlight %}

After Server and Client has been successfully setup, input any words from the client terminal (input string "Over" to stop the client-server connection), and they will appear on the server terminal.

<a name="codes"></a>
## Codes ([reference](https://www.geeksforgeeks.org/socket-programming-in-java/))
<details><summary>Client.java</summary>
<p>
{% highlight java %}
// A Java program for a client
import java.net.*;  // import all java class files contained in java.net path
import java.io.*;

public class Client{
  // initialize socket and input output streams
  private Socket socket = null;
  private DataInputStream input = null;
  private DataOutputStream out = null;

  // constructor to put ip address and port
  public Client(String address, int port)
  {
      // establish a connection
      try
      {
          socket = new Socket(address, port);
          System.out.println("Connected");

          // takes input from terminal
          input  = new DataInputStream(System.in);

          // sends output to the socket
          out    = new DataOutputStream(socket.getOutputStream());
      }
      catch(UnknownHostException u)
      {
          System.out.println(u);
      }
      catch(IOException i)
      {
          System.out.println(i);
      }

      // string to read message from input
      String line = "";

      // keep reading until "Over" is input
      while (!line.equals("Over"))
      {
          try
          {
              line = input.readLine();
              out.writeUTF(line);
          }
          catch(IOException i)
          {
              System.out.println(i);
          }
      }

      // close the connection
      try
      {
          input.close();
          out.close();
          socket.close();
      }
      catch(IOException i)
      {
          System.out.println(i);
      }
  }
  public static void main(String args[])
  {
      Client client = new Client("127.0.0.1", 5000);
  }
}
{% endhighlight %}
</p>
</details>

<details><summary>Server.java</summary>
<p>
{% highlight java %}
// A Java program for a Server
import java.net.*;
import java.io.*;

public class Server
{
    //initialize socket and input stream
    private Socket          socket   = null;
    private ServerSocket    server   = null;
    private DataInputStream in       = null;

    // constructor with port
    public Server(int port)
    {
        // starts server and waits for a connection
        try
        {
            server = new ServerSocket(port);
            System.out.println("Server started");

            System.out.println("Waiting for a client ...");

            socket = server.accept();
            System.out.println("Client accepted");

            // takes input from the client socket
            in = new DataInputStream(
                new BufferedInputStream(socket.getInputStream()));

            String line = "";

            // reads message from client until "Over" is sent
            while (!line.equals("Over"))
            {
                try
                {
                    line = in.readUTF();
                    System.out.println(line);

                }
                catch(IOException i)
                {
                    System.out.println(i);
                }
            }
            System.out.println("Closing connection");

            // close connection
            socket.close();
            in.close();
        }
        catch(IOException i)
        {
            System.out.println(i);
        }
    }

    public static void main(String args[])
    {
        Server server = new Server(5000);
    }
}
{% endhighlight %}
</p>
</details>
