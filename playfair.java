import java.io.*;

class playfair
{
		public static void main(String args[])throws IOException
		{
				String key;
				BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
				key = br.readLine();
				// Key has text key
				char[][] mat = new char[5][5];
				int count = 0;
				int count2 = 0;
				char aplha[] = {'a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
				int loop = 0;
				for(int x=0;x<5;x++)
				{
					for(int y=0;y<5;y++)
					{
						if(count<key.length())
						{
							mat[x][y] = key.charAt(count);
							loop++;
							
						}
						count++;
						
					}
				}
				System.out.println("Loop is"+loop);
				int loop2 = 0;
				for(int x=0;x<5;x++)
				{
					for(int y=0;y<5;y++)
					{
						if(loop2>=loop)
						{
							char element = aplha[count2];
							if(key.indexOf(element)<0)
							{
								//element not in string
								mat[x][y] = element;
								System.out.println("element is"+element);
							}
							count2++;
						}
						loop2++;
						System.out.println("Loop2 is"+loop2);	
					}
				}
				
				for(int x=0;x<5;x++)
				{
					for(int y=0;y<5;y++)
					{
						System.out.println("Location"+x+y+mat[x][y]);
					}
				}
		}
	
}
