while True:
    try:
        x = int(input('Enter a number: '))
        break
    # except:
    # except (ValueError,KeyboardInterrupt):
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('That\'s not a valid key!')
    except KeyError:
        print("Key error")
    finally:
        print('\nAttempted input\n')